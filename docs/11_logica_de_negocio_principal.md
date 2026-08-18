# 05 Core Logic

## Pipeline Neuronal
El sistema utiliza un pipeline lineal gestionado por `GenerationWorker`:
1. **DALL-E 3:** Genera una imagen base de 1024x1024 basada en un prompt estructurado (RSM).
2. **rembg:** Realiza la extracción del sujeto principal localmente usando el modelo U2-Net.
3. **Pillow:** Ejecuta el redimensionamiento multiescala y la conversión a formatos binarios específicos (ICO y BMP de 24 bits).

## Gestión de Estado
El estado de la generación se comunica a la UI mediante señales de Qt (`progress`, `finished`, `error`), permitiendo actualizaciones en tiempo real de la barra de progreso sin bloquear el hilo principal.
