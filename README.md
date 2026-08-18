# Suit Favicon - AI Asset Generator

Generador nativo de assets para software basado en IA. Crea logotipos, favicons multi-resolución e imágenes para instaladores (Inno Setup, NSIS, WiX) de forma automática.

## Requisitos
- Python 3.11+
- Una clave de API de OpenAI (DALL-E 3)
- Conexión a internet (para la generación inicial de la imagen)

## Instalación
1. Clonar el repositorio.
2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
   *Nota: La primera vez que se ejecute la eliminación de fondo, `rembg` descargará el modelo U2-Net automáticamente (~170MB).*

## Uso
1. Ejecuta `python main.py`.
2. Introduce tu API Key y el nombre del proyecto.
3. Define el estilo y elementos del logo en el asistente.
4. Espera a que el pipeline neuronal procese los assets.
5. Los archivos se generarán en la carpeta seleccionada con la estructura estandarizada para instaladores de Windows.

## Estructura de Salida
```text
[Proyecto]/
├── source/          # Logo base y transparente (1024x1024)
├── icons/           # .ico para App y Web
├── installers/      # Carpeta para Inno Setup, NSIS y WiX (.bmp)
└── metadata/        # Log de generación en JSON
```
