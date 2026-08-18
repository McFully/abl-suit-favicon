# GUARDIAN MODE - Suit Favicon

## 1. Protección de Estabilidad
- El Guardián debe verificar que `rembg` no rompa el entorno local por dependencias de ONNX.
- El Guardián debe asegurar que la API Key no se guarde en texto plano en los logs de auditoría.

## 2. Acciones Automáticas
- Si se detecta un error fatal en el pipeline, el sistema debe registrar el stack trace completo y revertir a la página de configuración.

## 3. Restricciones
- No se permite la eliminación de las pantallas del Wizard clásico.
- No se permite el uso de frameworks experimentales que no sean PySide6.
