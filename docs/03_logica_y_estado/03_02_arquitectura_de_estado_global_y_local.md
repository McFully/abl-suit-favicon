# 03_02: Arquitectura de Estado Global y Local - ABL Suit Favicon

## 📊 Estado de la Aplicación en `SuitWizard`
- `self.stack`: Instancia de `QStackedWidget` con índices:
  - `0`: `ProcessingEnginePage` (Ingreso de rutas)
  - `1`: `ProcessingPage` (Barra de progreso y log)
  - `2`: `FinishedPage` (Lista de resultados y acciones finales)
- `self.output_dir`: Ruta de salida seleccionada por el usuario.
- `self.worker`: Instancia activa de `GenerationWorker`.
