# 14 Environment Variables

La aplicación no utiliza archivos `.env` externos por seguridad. En su lugar, la **OpenAI API Key** se solicita directamente al usuario en el primer paso del asistente y se mantiene solo en memoria durante la sesión de generación.

Opcionalmente, el sistema puede extenderse para usar variables de entorno del sistema si se integra en pipelines de CI/CD.
