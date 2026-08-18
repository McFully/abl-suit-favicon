# 04_01: Sistema de Diseño Tokens y Estilos - ABL Suit Favicon

## 🎨 Hoja de Estilos QSS (`app/ui/styles.py`)

```css
QMainWindow {
    background-color: #121212;
}

QLabel {
    color: #FFFFFF;
    font-family: 'Segoe UI', sans-serif;
}

QLabel#Title {
    font-size: 20px;
    font-weight: bold;
    color: #4CAF50;
}

QFrame#Card {
    background-color: #1E1E1E;
    border-radius: 12px;
    border: 1px solid #333333;
}

QLineEdit {
    background-color: #2A2A2A;
    border: 1px solid #444444;
    border-radius: 6px;
    padding: 8px;
    color: #FFFFFF;
}

QPushButton {
    background-color: #2196F3;
    color: white;
    border: none;
    border-radius: 6px;
    padding: 10px;
    font-weight: bold;
}

QPushButton#Secondary {
    background-color: #424242;
}
```
