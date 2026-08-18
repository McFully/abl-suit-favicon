# 01_05: Mapa Forense de Directorios y Archivos - ABL Suit Favicon

```
ABL Suit Favicon/
├── main.py                          # Punto de entrada de la aplicación (QApplication)
├── config.json                      # Configuración global e Inno Setup paths
├── requirements.txt                 # Dependencias Python
├── build_all.ps1                    # Script PowerShell de compilación con PyInstaller
├── Lanzar_App.bat                   # Ejecutable de inicio rápido en Windows
├── logo.png                         # Ícono oficial de la aplicación
├── icono.ico                        # Ícono ICO ejecutable
├── wizard_header.png                # Asset de cabecera predeterminado
├── wizard_sidebar.png               # Asset de barra lateral predeterminado
├── DESIGN.md                        # Guía de diseño visual
├── VERSION.md                       # Control de versión semántica (1.0.0)
├── current_problems.md              # Registro de notas de desarrollo
├── app/
│   ├── __init__.py                  # Módulo paquete
│   ├── services/
│   │   ├── __init__.py
│   │   ├── api_service.py           # Cliente API OpenAI/Grok
│   │   ├── image_service.py         # Motor de edición de imágenes RemBG/PIL
│   │   ├── logger_service.py        # Gestor de logs auditados
│   │   └── project_service.py       # Scaffolding de carpetas de proyecto
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── wizard.py                # QMainWindow y gestor de pantallas
│   │   ├── pages.py                 # Pantallas 0, 1 y 2 del asistente
│   │   └── styles.py                # Hojas de estilo QSS
│   ├── utils/
│   │   └── __init__.py
│   └── workers/
│       ├── __init__.py
│       └── gen_worker.py            # Hilo asíncrono QThread de procesamiento
├── architecture/
│   └── critical_files.md
├── context/
│   └── system_health.md
├── installer/
│   ├── setup.iss                    # Script Inno Setup Compiler
│   └── LICENSE.txt                  # Licencia del instalador
├── logs/
│   └── audit.log                    # Archivo rotativo de logs de auditoría
└── rules/
    ├── guardian_mode.md
    └── SAFE_DEV_WORKFLOW.md
```
