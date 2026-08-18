# 01 Architecture

## Patrón de Diseño
La aplicación sigue una arquitectura modular inspirada en **MVC (Model-View-Controller)** y **Service-Oriented Architecture (SOA)** para Python/Qt:

- **Views (UI):** Implementadas en `app/ui/`, manejan la presentación y captura de datos mediante un flujo de "Asistente" (Wizard).
- **Services (Logic):** Ubicados en `app/services/`, encapsulan la lógica de negocio (APIs, procesamiento de imagen, gestión de archivos).
- **Workers (Concurrency):** Manejan la ejecución asíncrona mediante `QThread` para mantener la interfaz fluida durante tareas pesadas de IA.

## Flujo General
1. **Captura:** El usuario introduce parámetros de diseño y configuración.
2. **Generación (Cloud):** Se solicita la imagen base a la API de OpenAI.
3. **Procesamiento (Local):** Se descarga la imagen y se procesa localmente para eliminar el fondo.
4. **Transformación (Local):** Se generan múltiples variantes de tamaño y formato.
5. **Persistencia:** Se organiza el resultado en el sistema de archivos y se registran los eventos en logs.
