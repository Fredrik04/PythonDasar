import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

def button_clicked():
    print("Tombol diklik")

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Contoh Program PyQt")
window.setGeometry(100, 100, 300, 200)

button = QPushButton("Klik Saya", window)
button.setGeometry(100, 50, 100, 30)
button.clicked.connect(button_clicked)

window.show()

sys.exit(app.exec_())
