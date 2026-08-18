# DESIGN SYSTEM - Suit Favicon

## 1. Fundamentos Visuales
- **Paleta de Colores:**
  - Fondo Principal: `#121212` (Dark Grey/Black)
  - Fondo Contenedores: `#1E1E1E` (Surface)
  - Color Primario / Acento: `#3D5AFE` (Electric Blue)
  - Texto Primario: `#FFFFFF`
  - Texto Secundario: `#BBBBBB`
  - Bordes: `#333333`

## 2. Tipografía
- **Fuente:** `Segoe UI`, `Roboto`, `Helvetica`.
- **Pesos:** Normal (400) para cuerpo, Bold (700) para títulos y botones.

## 3. Componentes UI (Qt/PySide6)
- **Wizard:** Navegación lineal mediante `QStackedWidget`.
- **Botones:**
  - `Primary`: Fondo azul, bordes redondeados (6px), padding generoso.
  - `Secondary`: Fondo gris oscuro para acciones neutrales.
- **Inputs:** Fondo oscuro, borde sutil que cambia a azul al enfocar.
- **Cards:** Uso de `QFrame` con ID `Card` para agrupar elementos visuales.

## 4. Experiencia de Usuario (UX)
- **Feedback Constante:** Barra de progreso lineal y etiquetas de estado dinámicas durante el procesamiento.
- **Prevención de Errores:** Validación de campos obligatorios en cada paso del Wizard.
- **Atomicidad:** Si el proceso falla o se cancela, se informa al usuario y se permite el re-intento sin reiniciar toda la app.
