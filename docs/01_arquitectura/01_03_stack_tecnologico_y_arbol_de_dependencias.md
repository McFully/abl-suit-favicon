# 01_03: Stack Tecnológico y Árbol de Dependencias - ABL Suit Favicon

## 🛠️ Tecnologías Core

| Tecnología | Versión | Rol en el Sistema |
| :--- | :--- | :--- |
| **Python** | 3.13 / 3.14 (x64) | Lenguaje base del runtime |
| **PySide6** | 6.7+ | Framework de UI nativo Qt6 |
| **Pillow (PIL)** | 10.0+ | Procesamiento de imágenes ráster y conversión ICO/PNG/BMP |
| **rembg** | 2.0+ | Eliminación de fondos por Deep Learning (IS-Net General Use) |
| **onnxruntime** | 1.18+ | Inferencia local del modelo de IA rembg |
| **openai** | 1.0+ | Cliente API para invocación de Grok (`api.x.ai`) |
| **requests** | 2.31+ | Descargas HTTP de recursos de imágenes de la API |
| **Inno Setup** | 6.2+ | Empaquetador ejecutable de Windows (`installer/setup.iss`) |

## 📦 `requirements.txt` Completo
```text
PySide6>=6.7.0
Pillow>=10.0.0
rembg>=2.0.50
openai>=1.0.0
requests>=2.31.0
```
