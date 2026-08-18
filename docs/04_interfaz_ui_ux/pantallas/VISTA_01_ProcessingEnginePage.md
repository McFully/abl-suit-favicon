# Ficha Atómica: ProcessingEnginePage

- **Ubicación**: `app/ui/pages.py` (Clase `ProcessingEnginePage`)
- **Propósito**: Pantalla inicial para la selección de la imagen de entrada y el directorio de destino.
- **Componentes**: `QLineEdit` (Ruta imagen), `QLineEdit` (Ruta salida), `QPushButton` (Seleccionar), `QPushButton` (Explorar), `QPushButton` (Iniciar).
- **Eventos**:
  - `_on_browse_image()`: Abre `QFileDialog.getOpenFileName()`.
  - `_on_browse_output()`: Abre `QFileDialog.getExistingDirectory()`.
