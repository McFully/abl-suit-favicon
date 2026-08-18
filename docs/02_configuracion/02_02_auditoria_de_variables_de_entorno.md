# 02_02: Auditoría de Variables de Entorno y Configuración - ABL Suit Favicon

## ⚙️ Archivo `config.json`
El archivo `config.json` almacena las rutas base del sistema y configuraciones opcionales:

```json
{
    "base_output_dir": "output",
    "grok_api_key": "",
    "default_installer_paths": {
        "installers_inno": "installer/inno",
        "installers_nsis": "installer/nsis",
        "installers_wix": "installer/wix"
    }
}
```

- `base_output_dir`: Carpeta raíz predeterminada para guardar los paquetes de assets generados.
- `grok_api_key`: Clave API para invocar Grok Imagine si se requiere generación sintética por prompt.
