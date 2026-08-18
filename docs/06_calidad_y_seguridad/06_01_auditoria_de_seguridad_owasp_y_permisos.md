# 06_01: Auditoría de Seguridad - ABL Suit Favicon

- La aplicación se ejecuta de forma completamente local sin enviar datos de imágenes a servidores externos, excepto si el usuario habilita explícitamente la API de Grok.
- Validación estricta de existencia de rutas locales mediante `os.path.exists()` antes de procesar.
