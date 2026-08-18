# 01_01: Resumen Ejecutivo y Modelo de Negocio - ABL Suit Favicon

## 🎯 Visión General del Producto
**ABL Suit Favicon** (v1.0.0) es un software desktop profesional de procesamiento técnico y determinista de assets gráficos para aplicaciones de software y sistemas operativos. Desarrollado por **Antigravity Soft**, su objetivo principal es transformar logotipos e imágenes en bruto (PNG, JPG, WEBP, BMP) en un paquete completo de recursos gráficos optimizados para distribución e instalación.

## 👥 Usuarios Objetivos y Casos de Uso
1. **Desarrolladores de Software**: Generación instantánea de archivos `.ico` multirresolución de 16x16 hasta 256x256 píxeles, incluyendo el formato crítico de 128x128.
2. **Diseñadores UI/UX**: Extracción e higienización automática de fondos utilizando IA (`rembg` con arquitectura IS-Net).
3. **Ingenieros de Empaquetado e Instaladores**: Creación de banners e imágenes laterales (`wizard_sidebar.png` de 164x314 y `wizard_header.png` de 55x55) compatibles con Inno Setup, NSIS y WiX.

## 🔑 Características Clave y Diferenciadores Técnicos
- **Motor Élite Equilibrado**: Algoritmo de eliminación de fondo inteligente basado en IA (`isnet-general-use`) con alpha matting fino para preservar tipografías oscuras y bordes delgados.
- **Encuadre Centrado 1:1**: Auto-recorte inteligente (`trim_and_resize_to_fill`) que elimina márgenes transparentes sobrantes y escala el elemento gráfico conservando un padding del 5%.
- **Generador Multi-Resolución ICO**: Creación directa de archivos `.ico` encapsulando múltiples capas bitmap (16, 32, 48, 64, 128, 256 píxeles).
- **Integración opcional Grok API**: Conexión con endpoints de X.AI (`grok-imagine-image` y `grok-2-1212`) para generación sintética de conceptos de branding.
- **Interfaz Wizard Guiada**: Asistente visual fluido desarrollado en PySide6 (Qt6) estructurado en un selector de 3 estados sin pérdida de contexto.
