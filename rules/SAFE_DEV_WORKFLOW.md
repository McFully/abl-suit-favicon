# SAFE DEV WORKFLOW - Suit Favicon

## 1. Modificar
- Todo cambio en los servicios debe ser testeado de forma aislada.
- No modificar `main.py` sin verificar el arranque del sistema.

## 2. Verificar
- Tras cada cambio, ejecutar `python main.py` para asegurar que el GUI carga correctamente.
- Verificar que los logs en `logs/` se generan adecuadamente.

## 3. Rollback
- Si el sistema muestra pantalla negra o error de importación, revertir al último commit estable.

## 4. Batching
- No aplicar más de 5 mejoras estructurales por ciclo.
