# 18 Deployment

## Proceso de Empaquetado (Windows)
1. Ejecutar `build_all.ps1`.
2. El script invocará a **PyInstaller** para crear un directorio `dist/SuitFavicon` con todas las dependencias.
3. Se invocará al compilador de **Inno Setup** (`iscc.exe`) para empaquetar el directorio en un archivo `dist_installer/SuitFavicon_Setup.exe`.

## Requisitos de Despliegue
El instalador resultante es compatible con Windows 10 y Windows 11. No requiere instalación previa de Python por parte del usuario final.
