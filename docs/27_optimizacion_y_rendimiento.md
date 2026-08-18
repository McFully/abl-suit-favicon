# 16 Performance

## Optimización de IA Local
`rembg` utiliza el modelo U2-Net optimizado para CPU/GPU. La primera ejecución es más lenta debido a la carga del modelo en memoria RAM (~100-200MB).

## Concurrencia
El uso de `QThreadPool` y `QThread` asegura que las llamadas de red y el procesamiento pesado de imágenes no bloqueen el "Main Event Loop" de Qt, manteniendo la aplicación fluida con un consumo estable de CPU.

## Filtros de Imagen
Se utiliza `Image.Resampling.LANCZOS` en Pillow para garantizar la máxima fidelidad visual al reducir imágenes de 1024px a tamaños minúsculos como 16px.
