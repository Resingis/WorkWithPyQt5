from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QVBoxLayout
import sys


class Window(QWidget):
    def __init__(self,login):
        super(Window,self).__init__()
        self.resize(300,300)
        label = QLabel(self)
        #label.move(140,130)
        label.setText(login)
        label.show()
        self.vbox = QVBoxLayout(self)
        self.vbox.addWidget(label)
        self.setLayout(self.vbox)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window('hi')
    win.show()
    sys.exit(app.exec_())
