# Ficha Atómica: ProcessingPage

- **Ubicación**: `app/ui/pages.py` (Clase `ProcessingPage`)
- **Propósito**: Realimentación visual en tiempo real durante la ejecución del worker.
- **Componentes**: `QProgressBar` (0-100%), `QLabel` (Estado), `QTextEdit` (Consola de Logs en verde `#0F0`).
- **Métodos**: `update_progress(value, message)`.
