from PySide6.QtCore import QThread, Signal
import os
import time
from app.services.image_service import ImageService
from app.services.logger_service import LoggerService
from PIL import Image

class GenerationWorker(QThread):
    progress = Signal(int, str)
    finished = Signal(list)
    error = Signal(str)

    def __init__(self, config):
        super().__init__()
        self.config = config
        self.logger = LoggerService()
        self._is_cancelled = False
        self.generated_files = []

    def run(self):
        try:
            img_service = ImageService()
            source_image = self.config['source_image']
            base_output_dir = self.config['output_dir']

            # Create a unique subfolder for this specific run
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            image_name = os.path.splitext(os.path.basename(source_image))[0]
            output_dir = os.path.join(base_output_dir, f"assets_{image_name}_{timestamp}")

            if not os.path.exists(output_dir):
                os.makedirs(output_dir)

            # 1. INICIALIZACIÓN (10%)
            self.progress.emit(10, "Cargando imagen de entrada...")
            self.logger.log_event("Worker", "Inicio de procesamiento técnico", "START")
            
            if not os.path.exists(source_image):
                raise Exception("La imagen de entrada no existe.")

            # 2. ELIMINACIÓN DE FONDO Y RECORTE 1:1 (30%)
            self.progress.emit(30, "Iniciando Motor Élite Equilibrado: Protegiendo detalles...")
            logo_path = os.path.join(output_dir, "logo.png")
            img_service.remove_background(source_image, logo_path)
            
            # Optimize drawing proportion: trim transparency and fill square (almost full width/height)
            img = Image.open(logo_path)
            img_optimized = img_service.trim_and_resize_to_fill(img, target_size=512)
            img_optimized.save(logo_path, "PNG")
            
            self.generated_files.append("logo.png")
            
            transparent_logo_path = logo_path # Keep reference for next steps

            # 3. GENERACIÓN DE FAVICONS .ICO (50%)
            self.progress.emit(50, "Generando set de archivos .ico...")
            
            # Master favicon (128x128)
            favicon_master_path = os.path.join(output_dir, "favicon.ico")
            img_service.generate_ico(transparent_logo_path, favicon_master_path, sizes=[(128, 128)])
            self.generated_files.append("favicon.ico")
            
            # Other individual .ico sizes
            other_ico_sizes = [16, 32, 48, 64, 256]
            for size in other_ico_sizes:
                ico_filename = f"favicon_{size}x{size}.ico"
                ico_path = os.path.join(output_dir, ico_filename)
                img_service.generate_ico(transparent_logo_path, ico_path, sizes=[(size, size)])
                self.generated_files.append(ico_filename)

            # 4. (PASO ELIMINADO: ICONOS PNG NO REQUERIDOS)
            self.progress.emit(70, "Omitiendo generación de PNGs (solo .ico solicitado)...")

            # 5. ASSETS PARA INSTALADORES (PNG) (90%)
            self.progress.emit(90, "Generando recursos para instaladores (PNG)...")
            
            # Ensure the logo is square and transparent
            img_logo = Image.open(logo_path).convert("RGBA")
            
            # Wizard Sidebar (164x314)
            sidebar_path = os.path.join(output_dir, "wizard_sidebar.png")
            # Create a solid white background (as requested earlier for consistency)
            sidebar = Image.new("RGB", (164, 314), (255, 255, 255))
            logo_resized_side = img_logo.resize((164, 164), Image.Resampling.LANCZOS)
            sidebar.paste(logo_resized_side, (0, 75), mask=logo_resized_side)
            sidebar.save(sidebar_path, "PNG")
            self.generated_files.append("wizard_sidebar.png")

            # Wizard Header (55x55)
            header_path = os.path.join(output_dir, "wizard_header.png")
            header = Image.new("RGB", (55, 55), (255, 255, 255))
            header_logo = img_logo.resize((55, 55), Image.Resampling.LANCZOS)
            header.paste(header_logo, (0, 0), mask=header_logo)
            header.save(header_path, "PNG")
            self.generated_files.append("wizard_header.png")

            # 6. FINALIZACIÓN (100%)
            self.progress.emit(100, "Procesamiento completado con éxito.")
            self.logger.log_event("Worker", "Procesamiento completado", "OK")
            self.finished.emit(self.generated_files)

        except Exception as e:
            self.logger.log_error("Worker", f"Error en el motor de procesamiento: {str(e)}")
            self.error.emit(str(e))

    def cancel(self):
        self._is_cancelled = True
