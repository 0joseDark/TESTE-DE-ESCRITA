# pip install pyqt5
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

class OlaMundoJanela(QWidget):
    def __init__(self):
        super().__init__()

        # Título da janela
        self.setWindowTitle("Exemplo Qt - Olá Mundo")

        # Mensagem inicial
        self.label = QLabel("Clique no botão para dizer Olá!", self)

        # Botão
        self.botao = QPushButton("Dizer Olá", self)
        self.botao.clicked.connect(self.mostrar_mensagem)

        # Botão para sair
        self.botao_sair = QPushButton("Sair", self)
        self.botao_sair.clicked.connect(self.close)

        # Layout (organização dos widgets na janela)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.botao)
        layout.addWidget(self.botao_sair)

        self.setLayout(layout)

    def mostrar_mensagem(self):
        self.label.setText("Olá, mundo!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = OlaMundoJanela()
    janela.show()
    sys.exit(app.exec_())
