from random import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout 
app = QApplication([])
line = QVBoxLayout()
winner = QLabel("Узнай кто победитель?")
number = QLabel("?")
button = QPushButton("Сгенерировать:")
line.addWidget(winner, alignment = Qt.AlignCenter)
line.addWidget(number, alignment = Qt.AlignCenter)
line.addWidget(button, alignment = Qt.AlignCenter)
def show_winner():
    number = randint(0,99)
    winner.setText(str(number))
    winner.setText("Победитель:")
button.clicked.connect(show_winner)
main_win = QWidget()
main_win.setLayout(line)


main_win.setWindowTitle("Окно")
main_win.resize(400,400)


main_win.show()
app.exec_()
