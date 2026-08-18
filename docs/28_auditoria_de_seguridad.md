# 17 Security

- **API Keys:** No se guardan de forma persistente. Se solicitan por sesión y se mantienen en variables volátiles.
- **Auditoría:** `LoggerService` no registra claves de API ni datos sensibles del usuario.
- **Privacidad:** El procesamiento de eliminación de fondo es 100% local tras la descarga inicial de la imagen desde OpenAI.
- **Integridad:** El "Guardian Mode" en las reglas locales asegura que las dependencias no sean alteradas por scripts no autorizados.
