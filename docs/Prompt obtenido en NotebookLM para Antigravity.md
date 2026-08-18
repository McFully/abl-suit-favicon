Actúa como un Ingeniero de Software Senior y Arquitecto de Sistemas experto en Python y desarrollo de aplicaciones de escritorio para Windows. Tu tarea es desarrollar una aplicación de escritorio nativa para Windows enfocada en la generación automatizada de assets gráficos para software (logos, favicons multi-resolución e imágenes para instaladores tipo Setup Wizard) utilizando IA generativa y procesamiento neuronal local.

A continuación, se detallan los requisitos técnicos, arquitectónicos y de flujo de usuario que debes implementar obligatoriamente. Genera el código completo, modular y listo para producción.

### 1. ARQUITECTURA TÉCNICA Y TECNOLOGÍAS
La aplicación debe estar construida con las siguientes tecnologías, priorizando la simplicidad, la ejecución local eficiente y la robustez:
*   **Lenguaje:** Python 3.11+.
*   **Framework UI:** `PySide6` (Qt for Python). Ideal para integración fluida con librerías nativas de Python y menor consumo de RAM (aprox. 50-100 MB) comparado con Electron.
*   **Manejo de Concurrencia:** Obligatorio el uso de `QThread`, `QRunnable` y `QThreadPool` de PySide6 para ejecutar la generación de IA y el procesamiento de imágenes sin bloquear (freeze) la interfaz gráfica (Main GUI Thread).
*   **IA Generativa (Text-to-Image):** Integración con `OpenAI API (DALL-E 3)` o `Stability AI REST API (v2beta - sd3.5-large)`. Las llamadas deben ser asíncronas o manejadas en hilos secundarios.
*   **Procesamiento de Imágenes Local:**
    *   `rembg` (basado en U2-Net con *alpha matting*) para la eliminación precisa del fondo de forma local.
    *   `Pillow` (PIL) para redimensionamiento de alta calidad usando el filtro `Image.Resampling.LANCZOS`, manejo de canales Alpha (RGBA) y conversión a formatos `.ico`, `.bmp` y `.png`.

### 2. PIPELINE DE GENERACIÓN DE ASSETS
El sistema debe ejecutar de manera atómica e ininterrumpida el siguiente flujo de procesamiento al iniciar la generación:
1.  **Síntesis de Imagen (API IA):** Enviar un prompt optimizado a la API seleccionada para generar una imagen base de 1024x1024 px.
2.  **Extracción de Fondo (Local):** Pasar la imagen generada por la librería `rembg` activando `alpha matting` para aislar el logotipo y generar un PNG transparente (RGBA).
3.  **Redimensionamiento y Normalización (Local):** Escalar la imagen usando `Pillow` (Lanczos) para cubrir todas las especificaciones de instaladores y web.
4.  **Conversión y Ensamblado de Formatos (Local):**
    *   **ICO Multi-resolución:** Empaquetar resoluciones de 16x16, 32x32, 48x48, 64x64 y 256x256 px en un solo archivo `.ico` utilizando el guardado nativo de `Pillow` con múltiples tamaños.
    *   **Setup Wizards (BMP):** Generar los mapas de bits requeridos por los frameworks de instalación en formato `.bmp` estricto (24-bit RGB) cortando o adaptando el aspect ratio sin distorsión de la siguiente manera:
        *   *Inno Setup:* `wizard-image.bmp` (164x314), `small-image.bmp` (58x58).
        *   *NSIS (MUI2):* `welcome.bmp` (164x314), `header.bmp` (150x57).
        *   *WiX Toolset:* `dialog.bmp` (493x312 - adaptado al lado izquierdo para contraste), `banner.bmp` (493x58).

### 3. ESTRUCTURA DE CARPETAS AUTOMATIZADA
La aplicación debe requerir al usuario seleccionar una carpeta base y proveer el nombre del proyecto. Tras la ejecución exitosa, el sistema debe crear automáticamente la siguiente estructura jerárquica estandarizada:

```text
[Carpeta Seleccionada]/[Nombre del Proyecto]/
├── source/
│   ├── base_logo_1024.png
│   └── transparent_logo_1024.png
├── icons/
│   ├── app_icon.ico        # Multi-resolución (256, 64, 48, 32, 16)
│   └── favicon.ico         # Web optimizado (48, 32, 16)
├── installers/
│   ├── inno/
│   │   ├── wizard-image.bmp # 164x314
│   │   └── small-image.bmp  # 58x58
│   ├── nsis/
│   │   ├── welcome.bmp      # 164x314
│   │   └── header.bmp       # 150x57
│   └── wix/
│       ├── dialog.bmp       # 493x312
│       └── banner.bmp       # 493x58
└── metadata/
    └── generation_log.json  # Contiene prompt original, timestamp y configuraciones.
```

### 4. FLUJO DE USUARIO Y UI (WIZARD PATTERN)
Implementa una interfaz gráfica utilizando el patrón "Wizard" (Asistente paso a paso) en PySide6. La UI debe tener una navegación de tipo [Atrás] / [Siguiente].
*   **Paso 1: Configuración del Proyecto.**
    *   Campo para API Key (oculto por defecto).
    *   Campo de texto para Nombre del Proyecto.
    *   Selector de directorio de salida (Botón Browse).
*   **Paso 2: Generador de Prompt Optimizado (RSM).**
    *   En lugar de un campo de texto libre, utiliza campos estructurados basados en Response Surface Methodology para logos:
        *   Tema/Estilo (ej. Eco-friendly tech startup).
        *   Nombre/Texto en el logo.
        *   Tipo de Fuente (ej. Clean sans-serif).
        *   Color Principal y Color Secundario.
        *   Elementos Core (Máximo 3 elementos separados por coma).
    *   El sistema concatena estos campos en un prompt maestro interno.
*   **Paso 3: Procesamiento (Progress).**
    *   Barra de progreso lineal que muestre el estado de la tarea en hilos ("Conectando con API...", "Eliminando fondo localmente...", "Generando archivos ICO...", "Ensamblando BMPs...").
    *   Debe incluir un botón para cancelar o abortar.
*   **Paso 4: Finalización.**
    *   Vista previa de los assets principales (Logo transparente).
    *   Ruta del proyecto generado.
    *   Botón "Abrir carpeta en el Explorador de Windows" (usando `os.startfile`).

### 5. DIRECTRICES DE CÓDIGO
*   Escribe el código estructurado en Clases utilizando principios SOLID. Separa claramente la lógica de la UI (Views), los hilos de procesamiento (Workers/Controllers) y los servicios de las APIs y procesamiento de imágenes (Services).
*   Manejo exhaustivo de errores en cada nodo del pipeline (ej. fallo de red en la API, librerías faltantes, fallo de escritura de archivos).
*   Proporciona el código de Python principal (`main.py`) y las instrucciones exactas de dependencias (`requirements.txt`). No omitas ninguna función crítica para el redimensionamiento, recorte de imágenes o llamadas de API.