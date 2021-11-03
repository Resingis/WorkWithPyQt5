import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit,QHBoxLayout, QVBoxLayout, QPushButton

class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()



        # General VBoxLayout
        self.vbox = QVBoxLayout(self)

        # HBoxLayout
        self.hbox_input = QHBoxLayout()
        self.hbox_first = QHBoxLayout()
        self.hbox_result = QHBoxLayout()

        # Connect hbox and Layout
        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_first)
        self.vbox.addLayout(self.hbox_result)

        self.input = QLineEdit(self)
        self.input.setReadOnly(True)
        self.hbox_input.addWidget(self.input)

        # Button "1"
        self.b_1 = QPushButton("1", self)
        self.hbox_first.addWidget(self.b_1)

        # Button "2"
        self.b_2 = QPushButton("2", self)
        self.hbox_first.addWidget(self.b_2)
        # Button "3"

        self.b_3 = QPushButton("3", self)
        self.hbox_first.addWidget(self.b_3)

        # Button "4"
        self.b_4 = QPushButton("4", self)
        self.hbox_first.addWidget(self.b_4)

        # Button "4"
        self.b_5 = QPushButton("5", self)
        self.hbox_first.addWidget(self.b_5)

        # Button "6"
        self.b_6 = QPushButton("6", self)
        self.hbox_first.addWidget(self.b_6)

        # Button "7"
        self.b_7 = QPushButton("7", self)
        self.hbox_first.addWidget(self.b_7)

        # Button "8"
        self.b_8 = QPushButton("8", self)
        self.hbox_first.addWidget(self.b_8)

        # Button "9"
        self.b_9 = QPushButton("9", self)
        self.hbox_first.addWidget(self.b_9)

        # Button "0"
        self.b_0 = QPushButton("0", self)
        self.hbox_first.addWidget(self.b_0)

        # Button "+"
        self.b_plus = QPushButton("+", self)
        self.hbox_first.addWidget(self.b_plus)
        # Button "-"
        self.b_minus = QPushButton("-", self)
        self.hbox_first.addWidget(self.b_minus)
        # Button "*"
        self.b_multiplication = QPushButton("*", self)
        self.hbox_first.addWidget(self.b_multiplication)
        # Button "/"
        self.b_division = QPushButton("/", self)
        self.hbox_first.addWidget(self.b_division)

        # Button "="
        self.b_result = QPushButton("=", self)
        self.hbox_result.addWidget(self.b_result)

        # Push button "+"
        self.b_plus.clicked.connect(lambda: self.operation("+"))

        # Push button "-"
        self.b_minus.clicked.connect(lambda: self.operation("-"))

        # Push button "*"
        self.b_multiplication.clicked.connect(lambda: self.operation("*"))

        # Push button "/"
        self.b_division.clicked.connect(lambda: self.operation("/"))

        # Push button "="
        self.b_result.clicked.connect(self._result)

        # Push button of number
        self.b_1.clicked.connect(lambda: self._button("1"))
        self.b_2.clicked.connect(lambda: self._button("2"))
        self.b_3.clicked.connect(lambda: self._button("3"))
        self.b_4.clicked.connect(lambda: self._button("4"))
        self.b_5.clicked.connect(lambda: self._button("5"))
        self.b_6.clicked.connect(lambda: self._button("6"))
        self.b_7.clicked.connect(lambda: self._button("7"))
        self.b_8.clicked.connect(lambda: self._button("8"))
        self.b_9.clicked.connect(lambda: self._button("9"))
        self.b_0.clicked.connect(lambda: self._button("0"))

    def _button (self, param):
        line = self.input.text()
        self.input.setText(line + param)


    def operation(self, op):
        self.num_1 = int(self.input.text())
        self.op = op
        self.input.setText("")

    def _result(self):
        self.num_2 = int(self.input.text())
        if self.op == "+":
            self.input.setText(str(self.num_1 + self.num_2))
        if self.op == "-":
            self.input.setText(str(self.num_1 - self.num_2))
        if self.op == "*":
            self.input.setText(str(self.num_1 * self.num_2))
        if self.op == "/":
            self.input.setText(str(self.num_1 / self.num_2))
        elif self.op == "=":
            pass
        if self.num_2 == "" and self.num_2 == " ":
            self.input.setText("Error")


app = QApplication(sys.argv)

win = Calculator()
win.show()

sys.exit(app.exec_())