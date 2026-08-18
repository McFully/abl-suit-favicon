PROMPT - GENERACIÓN COMPLETA DE DOCUMENTACIÓN DEL PROYECTO (FORMATO MARKDOWN)

Actúa como un arquitecto de software senior especializado en documentación técnica profesional. Analiza TODO el código fuente del proyecto actual y genera una documentación completa, estructurada y lista para entrega en una carpeta llamada /docs.

OBJETIVO:
Crear documentación técnica exhaustiva que permita a cualquier desarrollador, técnico o stakeholder entender completamente el proyecto sin necesidad de revisar el código.

INSTRUCCIONES:

1. ESTRUCTURA DE CARPETAS
Genera la siguiente estructura dentro de /docs:

/docs
  ├── 00_overview.md
  ├── 01_architecture.md
  ├── 02_tech_stack.md
  ├── 03_setup_installation.md
  ├── 04_project_structure.md
  ├── 05_core_logic.md
  ├── 06_features.md
  ├── 07_data_flow.md
  ├── 08_api_endpoints.md (si aplica)
  ├── 09_database.md (si aplica)
  ├── 10_state_management.md (si aplica)
  ├── 11_ui_ux.md
  ├── 12_game_mechanics.md (si es un juego)
  ├── 13_config_files.md
  ├── 14_environment_variables.md
  ├── 15_testing.md
  ├── 16_performance.md
  ├── 17_security.md
  ├── 18_deployment.md
  ├── 19_known_issues.md
  ├── 20_future_improvements.md
  └── 99_glossary.md

2. CONTENIDO DETALLADO

- 00_overview.md:
  Explicación clara del proyecto, propósito, problema que resuelve y resultado final.

- 01_architecture.md:
  Descripción de la arquitectura (frontend/backend, módulos, patrones, flujo general).

- 02_tech_stack.md:
  Tecnologías utilizadas con explicación de por qué se eligieron.

- 03_setup_installation.md:
  Pasos exactos para instalar, configurar y ejecutar el proyecto.

- 04_project_structure.md:
  Explicación completa de carpetas y archivos importantes.

- 05_core_logic.md:
  Desglose de la lógica principal del sistema o del juego.

- 06_features.md:
  Lista detallada de funcionalidades implementadas.

- 07_data_flow.md:
  Cómo fluye la información dentro del sistema.

- 08_api_endpoints.md:
  Documentación de endpoints (si existen).

- 09_database.md:
  Estructura de base de datos, tablas, relaciones (si aplica).

- 10_state_management.md:
  Gestión de estado (si aplica).

- 11_ui_ux.md:
  Estructura visual, interacción, decisiones de diseño.

- 12_game_mechanics.md:
  Explicación completa de mecánicas del juego (física, colisiones, lógica de gameplay, etc.).

- 13_config_files.md:
  Explicación de archivos de configuración.

- 14_environment_variables.md:
  Variables necesarias y su función.

- 15_testing.md:
  Estrategia de testing (si existe).

- 16_performance.md:
  Consideraciones de rendimiento.

- 17_security.md:
  Medidas de seguridad implementadas (si aplica).

- 18_deployment.md:
  Cómo desplegar el proyecto.

- 19_known_issues.md:
  Problemas conocidos.

- 20_future_improvements.md:
  Posibles mejoras.

- 99_glossary.md:
  Definiciones de términos técnicos usados.

3. REGLAS DE GENERACIÓN

- Usa Markdown profesional con encabezados claros (#, ##, ###).
- Incluye ejemplos de código cuando sea útil.
- Explica todo de forma clara pero técnica.
- No omitas ninguna parte relevante del sistema.
- Deduce información faltante a partir del código si es necesario.
- Prioriza claridad, precisión y completitud.

4. ESTILO

- Lenguaje técnico profesional.
- Explicaciones estructuradas.
- Pensado para que otra persona pueda mantener o escalar el proyecto.

Genera TODOS los archivos con su contenido completo.