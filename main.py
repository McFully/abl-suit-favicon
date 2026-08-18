import sys
from PySide6.QtWidgets import QApplication
from app.ui.wizard import SuitWizard
from app.services.logger_service import LoggerService

def main():
    logger = LoggerService()
    logger.log_event("Core", "Iniciando Aplicación", "START")
    
    app = QApplication(sys.argv)
    
    # Set default font to avoid "PointSize <= 0" warnings on some Windows systems
    from PySide6.QtGui import QFont
    default_font = QFont("Segoe UI", 10)
    app.setFont(default_font)
    
    # Set application metadata
    app.setApplicationName("Suit Favicon")
    app.setOrganizationName("Antigravity Soft")
    
    window = SuitWizard()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
