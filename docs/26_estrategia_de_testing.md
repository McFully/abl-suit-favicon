# 15 Testing

## Estrategia
Se recomienda realizar pruebas de integración para:
1. **API Connectivity:** Validar que el `APIService` maneja errores de timeout y cuotas.
2. **Image Integrity:** Verificar que los BMPs generados por `ImageService` abren correctamente en visores nativos de Windows.
3. **UI Flow:** Testing manual de las transiciones del Wizard y cancelación de tareas en progreso.
