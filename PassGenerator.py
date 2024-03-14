import sys
import random
import string
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QMessageBox

class PasswordGeneratorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Password Generator')
        self.setGeometry(100, 100, 300, 200)

        self.password_label = QLabel('Generated Password:', self)
        self.password_output = QLineEdit(self)
        self.password_output.setReadOnly(True)

        self.length_label = QLabel('Length:', self)
        self.length_input = QLineEdit(self)

        self.generate_button = QPushButton('Generate Password', self)
        self.generate_button.clicked.connect(self.generate_password)

        layout = QVBoxLayout()
        layout.addWidget(self.length_label)
        layout.addWidget(self.length_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_output)
        layout.addWidget(self.generate_button)

        self.setLayout(layout)

    def generate_password(self):
        try:
            length = int(self.length_input.text())
            if length <= 0:
                QMessageBox.critical(self, 'Error', 'Length must be a positive integer.')
                return
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))
            self.password_output.setText(password)
        except ValueError:
            QMessageBox.critical(self, 'Error', 'Invalid input. Please enter a valid integer.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PasswordGeneratorApp()
    window.show()
    sys.exit(app.exec_())
