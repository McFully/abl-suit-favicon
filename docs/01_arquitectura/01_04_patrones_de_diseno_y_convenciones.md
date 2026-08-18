# 01_04: Patrones de Diseño y Convenciones - ABL Suit Favicon

## 🎨 Patrones Arquitectónicos Aplicados

1. **Model-View-Worker (MVW / Async Processing)**:
   - La UI (`SuitWizard`, `QStackedWidget`) nunca ejecuta tareas de I/O o procesamiento gráfico en el hilo principal de eventos (`GUI Thread`).
   - `GenerationWorker` encapsula el trabajo en un `QThread` y transmite métricas mediante `PySide6.QtCore.Signal`.

2. **Singleton Pattern**:
   - `LoggerService` implementa `__new__` para garantizar una única instancia global del logger escribiendo en `logs/audit.log`.

3. **Lazy Session Initialization**:
   - `ImageService._get_session()` carga el modelo pesadísimo de IA (`isnet-general-use`) bajo demanda solo cuando el usuario arranca el proceso, evitando latencias al abrir la app.

4. **Service Object Pattern**:
   - Métodos estáticos puros en `ImageService` y `ProjectService` encargados de responsabilidades únicas (SRP).
