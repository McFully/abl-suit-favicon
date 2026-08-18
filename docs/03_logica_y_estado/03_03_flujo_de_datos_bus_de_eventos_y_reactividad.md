# 03_03: Flujo de Datos y Reactividad mediante Signals - ABL Suit Favicon

## ⚡ PySide6 Signals en `GenerationWorker`
- `progress = Signal(int, str)`: Emite el porcentaje (0-100) y la descripción del paso.
- `finished = Signal(list)`: Emite la lista de nombres de archivos generados.
- `error = Signal(str)`: Emite el mensaje de excepción en caso de fallo técnico.
