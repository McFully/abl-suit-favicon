MAIN_STYLE = """
QMainWindow {
    background-color: #121212;
}

QWidget {
    background-color: #121212;
    color: #E0E0E0;
    font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    font-size: 14px;
}

QLabel {
    color: #BBBBBB;
}

QLabel#Title {
    font-size: 24px;
    font-weight: bold;
    color: #FFFFFF;
    margin-bottom: 10px;
}

QLineEdit {
    background-color: #1E1E1E;
    border: 1px solid #333333;
    border-radius: 6px;
    padding: 8px;
    color: #FFFFFF;
    selection-background-color: #3D5AFE;
}

QLineEdit:focus {
    border: 1px solid #3D5AFE;
}

QPushButton {
    background-color: #3D5AFE;
    color: white;
    border: none;
    border-radius: 6px;
    padding: 10px 20px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #536DFE;
}

QPushButton:pressed {
    background-color: #303F9F;
}

QPushButton#Secondary {
    background-color: #333333;
}

QPushButton#Secondary:hover {
    background-color: #444444;
}

QProgressBar {
    border: 1px solid #333333;
    border-radius: 5px;
    text-align: center;
    background-color: #1E1E1E;
}

QProgressBar::chunk {
    background-color: #3D5AFE;
    width: 20px;
}

QFrame#Card {
    background-color: #1E1E1E;
    border-radius: 12px;
    border: 1px solid #333333;
}

QScrollArea {
    border: none;
}

QTextEdit {
    background-color: #1E1E1E;
    border: 1px solid #333333;
    border-radius: 8px;
    padding: 10px;
    color: #E0E0E0;
}
"""
