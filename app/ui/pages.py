from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                             QLineEdit, QPushButton, QFileDialog, QProgressBar, 
                             QStackedWidget, QFrame, QTextEdit)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QPixmap

class ProcessingEnginePage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(50, 50, 50, 50)
        layout.setSpacing(25)

        title = QLabel("Suit Favicon: Procesador Técnico de Assets")
        title.setObjectName("Title")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        subtitle = QLabel("Transformación determinista de imágenes en assets de software")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("color: #888; font-size: 14px; margin-bottom: 20px;")
        layout.addWidget(subtitle)

        # Container for inputs
        card = QFrame()
        card.setObjectName("Card")
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(30, 30, 30, 30)
        card_layout.setSpacing(15)

        # Image selection
        card_layout.addWidget(QLabel("IMAGEN DE ENTRADA (ORIGEN)"))
        h_layout_img = QHBoxLayout()
        self.image_path = QLineEdit()
        self.image_path.setPlaceholderText("Selecciona el logo o imagen base...")
        self.browse_img_btn = QPushButton("Seleccionar")
        self.browse_img_btn.setObjectName("Secondary")
        self.browse_img_btn.setFixedWidth(100)
        self.browse_img_btn.clicked.connect(self._on_browse_image)
        h_layout_img.addWidget(self.image_path)
        h_layout_img.addWidget(self.browse_img_btn)
        card_layout.addLayout(h_layout_img)

        # Output selection
        card_layout.addWidget(QLabel("CARPETA DE SALIDA (DESTINO)"))
        h_layout_out = QHBoxLayout()
        self.output_path = QLineEdit()
        self.output_path.setPlaceholderText("C:/Ruta/De/Destino")
        self.browse_out_btn = QPushButton("Explorar")
        self.browse_out_btn.setObjectName("Secondary")
        self.browse_out_btn.setFixedWidth(100)
        self.browse_out_btn.clicked.connect(self._on_browse_output)
        h_layout_out.addWidget(self.output_path)
        h_layout_out.addWidget(self.browse_out_btn)
        card_layout.addLayout(h_layout_out)

        layout.addWidget(card)

        layout.addStretch()

        self.process_btn = QPushButton("INICIAR PROCESAMIENTO TÉCNICO")
        self.process_btn.setMinimumHeight(60)
        self.process_btn.setStyleSheet("font-size: 16px; font-weight: bold; background: #2E7D32; color: white;")
        layout.addWidget(self.process_btn)

    def _on_browse_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Seleccionar Imagen", "", "Imágenes (*.png *.jpg *.jpeg *.webp *.bmp)")
        if file_path:
            self.image_path.setText(file_path)

    def _on_browse_output(self):
        path = QFileDialog.getExistingDirectory(self, "Seleccionar Carpeta de Salida")
        if path:
            self.output_path.setText(path)

    def get_data(self):
        return {
            "source_image": self.image_path.text(),
            "output_dir": self.output_path.text()
        }

class ProcessingPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(50, 50, 50, 50)
        layout.setSpacing(30)

        self.title = QLabel("Procesando Assets...")
        self.title.setObjectName("Title")
        self.title.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.title)

        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(True)
        self.progress_bar.setFormat("%p%")
        layout.addWidget(self.progress_bar)

        self.status_label = QLabel("Validando archivos...")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("color: #AAA; font-size: 14px;")
        layout.addWidget(self.status_label)

        self.log_display = QTextEdit()
        self.log_display.setReadOnly(True)
        self.log_display.setPlaceholderText("Logs de procesamiento...")
        self.log_display.setStyleSheet("background: #111; color: #0F0; font-family: 'Consolas'; font-size: 11px;")
        layout.addWidget(self.log_display)

    def update_progress(self, value, message):
        self.progress_bar.setValue(value)
        self.status_label.setText(message)
        self.log_display.append(f"[{value}%] {message}")

class FinishedPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(50, 50, 50, 50)
        layout.setSpacing(20)

        icon = QLabel("📦")
        icon.setStyleSheet("font-size: 64px;")
        icon.setAlignment(Qt.AlignCenter)
        layout.addWidget(icon)

        title = QLabel("Paquete de Assets Listo")
        title.setObjectName("Title")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        self.file_list = QTextEdit()
        self.file_list.setReadOnly(True)
        self.file_list.setStyleSheet("background: #222; border-radius: 8px; padding: 10px;")
        layout.addWidget(QLabel("Archivos generados:"))
        layout.addWidget(self.file_list)

        self.open_folder_btn = QPushButton("Abrir Carpeta de Assets")
        layout.addWidget(self.open_folder_btn)
        
        self.process_another_btn = QPushButton("Procesar Otra Imagen")
        self.process_another_btn.setObjectName("Primary")
        layout.addWidget(self.process_another_btn)

        self.finish_btn = QPushButton("Finalizar Aplicación")
        self.finish_btn.setObjectName("Secondary")
        layout.addWidget(self.finish_btn)

        layout.addStretch()

    def set_files(self, files):
        self.file_list.clear()
        for f in files:
            self.file_list.append(f"• {f}")
