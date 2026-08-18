# 07 Data Flow

1. **Input:** Usuario introduce API Key y datos del logo.
2. **Request:** `APIService` envía prompt a OpenAI.
3. **Response:** OpenAI devuelve URL de imagen -> `APIService` descarga bytes.
4. **Transform:** `ImageService` aplica rembg -> `transparent.png`.
5. **Scale:** `ImageService` redimensiona -> `app_icon.ico` y `*.bmp`.
6. **Output:** `ProjectService` guarda en la estructura de carpetas final.
7. **Log:** `LoggerService` registra el éxito o fracaso de cada paso.
