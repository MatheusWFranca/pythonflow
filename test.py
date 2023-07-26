import sys
import requests
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QMessageBox


def send_request():
    try:
        url = ''
        data = {
            "headers": {
                "email": "@example.com",
                "name": "",
                "twitter": "@",
                "github": ""
            }
        }

        response = requests.post(url, data=data)
        response.raise_for_status()
        QMessageBox.information(None, "Resposta HTTP",
                                "Requisição enviada com sucesso!")
    except requests.exceptions.RequestException as e:
        QMessageBox.critical(None, "Erro de Requisição", f"Erro: {e}")


def create_window():
    app = QApplication(sys.argv)

    window = QMainWindow()
    window.setWindowTitle("Exemplo de Tela em PySide6")
    window.setGeometry(100, 100, 400, 200)

    central_widget = QWidget()
    window.setCentralWidget(central_widget)

    layout = QVBoxLayout(central_widget)

    label = QLabel("Olá, esta é a minha tela em PySide6!", window)
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    button_layout = QHBoxLayout()

    button = QPushButton("Enviar Requisição POST", window)
    button.clicked.connect(send_request)

    button_layout.addWidget(button)

    layout.addWidget(label)
    layout.addLayout(button_layout)

    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    create_window()
