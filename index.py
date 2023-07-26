import sys
import requests
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QLineEdit, QFormLayout, QMessageBox


def send_request(data):
    try:
        url = API_KEY

        response = requests.post(url, json=data)
        response.raise_for_status()
        QMessageBox.information(None,
                                "Resposta HTTP",
                                "Requisição enviada com sucesso!")

    except requests.exceptions.RequestException as e:
        QMessageBox.critical(None, "Erro de Requisição", f"Erro: {e}")


def save_form_data(form_layout):
    data = {}
    for i in range(form_layout.count()):
        item = form_layout.itemAt(i)
        if isinstance(item.widget(), QLineEdit):
            key = item.widget().objectName()
            value = item.widget().text()
            data[key] = value

    headers = {
        "email": data.get("email"),
        "name": data.get("nome"),
        "twitter": data.get("twitter"),
        "github": data.get("github")
    }

    print("Dados do formulário salvos:")
    print(headers)

    return {"headers": headers}


def create_window():
    app = QApplication(sys.argv)

    window = QMainWindow()
    window.setWindowTitle("Exemplo de Tela em PySide6")
    window.setGeometry(100, 100, 400, 300)

    central_widget = QWidget()
    window.setCentralWidget(central_widget)

    layout = QVBoxLayout(central_widget)

    form_layout = QFormLayout()

    email_input = QLineEdit()
    email_input.setObjectName("email")
    form_layout.addRow("Email:", email_input)

    nome_input = QLineEdit()
    nome_input.setObjectName("nome")
    form_layout.addRow("Nome:", nome_input)

    twitter_input = QLineEdit()
    twitter_input.setObjectName("twitter")
    form_layout.addRow("Twitter:", twitter_input)

    github_input = QLineEdit()
    github_input.setObjectName("github")
    form_layout.addRow("Github:", github_input)

    layout.addLayout(form_layout)

    button_layout = QHBoxLayout()

    save_button = QPushButton("Salvar")

    save_button.clicked.connect(lambda: save_form_data(form_layout))
    button_layout.addWidget(save_button)

    send_button = QPushButton("Enviar Requisição POST")
    send_button.clicked.connect(
        lambda: send_request(save_form_data(form_layout)))
    button_layout.addWidget(send_button)

    layout.addLayout(button_layout)

    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    create_window()
