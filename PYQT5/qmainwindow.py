from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QMainWindow

app = QApplication([])

window = QMainWindow()
#label = QLabel("Label 1", window) # cara 1
label = QLabel(window)             # cara 2
label.setText("Label1")
label.move(200, 0)

#button = QpushButton("MyButton", window ) # cara 1
button = QPushButton(window)               # cara 2
button.setText("Button1")

window.show()
app.exec_()