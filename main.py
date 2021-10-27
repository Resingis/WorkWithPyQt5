from PyQt5.QtWidgets import QLabel, QApplication, QWidget, QPushButton, QMessageBox
import sys
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    label = QLabel(w)
    label.setText("Hello, world")
    label.move(100,130)
    label.show()
    w.resize(300,300)
    w.setWindowTitle('Guru96_EMPEROR')
    btn = QPushButton(w)
    btn.setText("Click")
    btn.move(110, 150)

    def dialog():
        mbox = QMessageBox()

        mbox.setText("Hey")
        mbox.setDetailedText("Hi")
        mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        mbox.exec_()
    btn.show()
    btn.clicked.connect(dialog)

    w.show()

    sys.exit(app.exec_())