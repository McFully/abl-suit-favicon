# 19 Known Issues

- **rembg Download:** La descarga del modelo U2-Net puede fallar si no hay conexión estable, causando un error en el primer procesamiento.
- **DALL-E 3 Cost:** El uso intensivo de la aplicación consume créditos de la API de OpenAI.
- **onnxruntime:** Dependiendo del hardware del usuario, `rembg` puede emitir warnings si no se encuentra soporte para aceleración por GPU (CUDA), aunque funcionará por CPU.
