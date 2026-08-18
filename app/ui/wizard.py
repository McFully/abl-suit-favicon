from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QStackedWidget, QMessageBox)
from PySide6.QtCore import Qt
import os
import json
from PySide6.QtGui import QIcon
from app.ui.pages import ProcessingEnginePage, ProcessingPage, FinishedPage
from app.ui.styles import MAIN_STYLE
from app.workers.gen_worker import GenerationWorker 

class SuitWizard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Suit Favicon v1.0.0 - Procesador de Assets de Software")
        self.setFixedSize(650, 750)
        self.setStyleSheet(MAIN_STYLE)
        
        # Set Application Icon
        if os.path.exists("logo.png"):
            self.setWindowIcon(QIcon("logo.png"))

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.stack = QStackedWidget()
        self.layout.addWidget(self.stack)

        # Pages
        self.engine_page = ProcessingEnginePage()
        self.processing_page = ProcessingPage()
        self.finished_page = FinishedPage()

        self.stack.addWidget(self.engine_page)      # Index 0
        self.stack.addWidget(self.processing_page)  # Index 1
        self.stack.addWidget(self.finished_page)    # Index 2

        # Connections
        self.engine_page.process_btn.clicked.connect(self._start_processing)
        self.finished_page.open_folder_btn.clicked.connect(self._open_folder)
        self.finished_page.process_another_btn.clicked.connect(self._reset_wizard)
        self.finished_page.finish_btn.clicked.connect(self.close)

        # Worker
        self.worker = None
        self.output_dir = None
        self.last_assets_dir = None

    def _start_processing(self):
        data = self.engine_page.get_data()
        
        if not data['source_image'] or not os.path.exists(data['source_image']):
            QMessageBox.warning(self, "Error", "Debes seleccionar una imagen de entrada válida.")
            return
        
        if not data['output_dir'] or not os.path.exists(data['output_dir']):
            QMessageBox.warning(self, "Error", "Debes seleccionar una carpeta de salida válida.")
            return

        self.output_dir = data['output_dir']
        self.stack.setCurrentIndex(1) # Processing
        
        # Reset progress bar for new run
        self.processing_page.update_progress(0, "Iniciando motor...")
        
        # Start Worker
        self.worker = GenerationWorker(data)
        self.worker.progress.connect(self.processing_page.update_progress)
        self.worker.finished.connect(self._on_finished)
        self.worker.error.connect(self._on_error)
        self.worker.start()

    def _on_finished(self, files):
        # The worker now returns (files, subfolder_path) or we can infer it
        # Let's assume we capture the output dir from the worker if needed
        # Or just use the last one generated
        if files:
            # The files are relative to the subfolder, let's find the subfolder
            # Since we know the output_dir and the timestamp/name logic
            # Let's update the worker to emit the final directory
            pass
        
        self.finished_page.set_files(files)
        self.stack.setCurrentIndex(2) # Finished

    def _reset_wizard(self):
        # Clear source image but keep output dir
        self.engine_page.image_path.clear()
        self.stack.setCurrentIndex(0)
        # Automatically trigger the file selection to speed up the workflow
        self.engine_page._on_browse_image()

    def _on_error(self, msg):
        QMessageBox.critical(self, "Error de Procesamiento", f"El sistema no pudo completar la tarea: {msg}")
        self.stack.setCurrentIndex(0)

    def _open_folder(self):
        # Open the base output directory (the one set by the user)
        if self.output_dir and os.path.exists(self.output_dir):
            os.startfile(self.output_dir)
