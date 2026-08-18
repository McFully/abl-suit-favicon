# 02_04: Scripts y Automatizaciones CLI - ABL Suit Favicon

## 📜 Script `build_all.ps1` (PowerShell)
Automatiza la compilación del binario `.exe` utilizando PyInstaller:

```powershell
pyinstaller --noconfirm --onedir --windowed `
    --add-data "logo.png;." `
    --add-data "icono.ico;." `
    --icon "icono.ico" `
    --name "SuitFavicon" `
    main.py
```
