# 02_03: Análisis de Archivos de Configuración - ABL Suit Favicon

## 📄 Archivo `installer/setup.iss` (Inno Setup Compiler)
Define las reglas de empaquetado del instalador Windows ejecutable:

- **AppId**: `{#SetupSetting("AppName")}`
- **AppName**: `Suit Favicon`
- **AppVersion**: `1.0.0`
- **AppPublisher**: `Antigravity Soft`
- **DefaultDirName**: `{autopf}\Suit Favicon`
- **WizardImageFile**: `wizard_sidebar.bmp` (164x314)
- **WizardSmallImageFile**: `wizard_header.bmp` (55x55)
