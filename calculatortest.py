import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow


style_sheet = """
        QWidget {
            background-color:orange;
        }
        QPushButton {
            background-color:white;
            border-radius:7px;
            border-size:15px;
            font-size:15px;
        }"""

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Калькулятор")
        self.setGeometry(300, 300, 375, 375)
        self.result = ""



        self.main_text = QtWidgets.QLabel(self)
        self.flag = True
        self.main_text.setText("")
        self.main_text.setGeometry(50, 50, 300, 10)
      
        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.resize(50,50)
        self.btn1.move(10,100)
        self.btn1.setText("1")
        self.btn1.clicked.connect(self.btn1_handler)

        self.btn2 = QtWidgets.QPushButton(self)
        self.btn2.resize(50,50)
        self.btn2.move(70,100)
        self.btn2.setText("2")
        self.btn2.clicked.connect(self.btn2_handler)

        self.btn3 = QtWidgets.QPushButton(self)
        self.btn3.resize(50,50)
        self.btn3.move(130,100)
        self.btn3.setText("3")
        self.btn3.clicked.connect(self.btn3_handler)

        self.btn4 = QtWidgets.QPushButton(self)
        self.btn4.resize(50,50)
        self.btn4.move(10,170)
        self.btn4.setText("4")
        self.btn4.clicked.connect(self.btn4_handler)
        
        self.btn5 = QtWidgets.QPushButton(self)
        self.btn5.resize(50,50)
        self.btn5.move(70,170)
        self.btn5.setText("5")
        self.btn5.clicked.connect(self.btn5_handler)

        self.btn6 = QtWidgets.QPushButton(self)
        self.btn6.resize(50,50)
        self.btn6.move(130,170)
        self.btn6.setText("6")
        self.btn6.clicked.connect(self.btn6_handler)

        self.btn7 = QtWidgets.QPushButton(self)
        self.btn7.resize(50,50)
        self.btn7.move(10,240)
        self.btn7.setText("7")
        self.btn7.clicked.connect(self.btn7_handler)

        self.btn8 = QtWidgets.QPushButton(self)
        self.btn8.resize(50,50)
        self.btn8.move(70,240)
        self.btn8.setText("8")
        self.btn8.clicked.connect(self.btn8_handler)

        self.btn9 = QtWidgets.QPushButton(self)
        self.btn9.resize(50,50)
        self.btn9.move(130,240)
        self.btn9.setText("9")
        self.btn9.clicked.connect(self.btn9_handler)

        self.btnclear = QtWidgets.QPushButton(self)
        self.btnclear.resize(50,50)
        self.btnclear.move(190,240)
        self.btnclear.setText("C")
        self.btnclear.clicked.connect(self.btnclear_handler)

        self.btn0 = QtWidgets.QPushButton(self)
        self.btn0.resize(50,50)
        self.btn0.move(70,310)
        self.btn0.setText("0")
        self.btn0.clicked.connect(self.btn0_handler)

        self.btnplus = QtWidgets.QPushButton(self)
        self.btnplus.resize(50,50)
        self.btnplus.move(10,310)
        self.btnplus.setText("+")
        self.btnplus.clicked.connect(self.btnplus_handler)

        self.btnminus = QtWidgets.QPushButton(self)
        self.btnminus.resize(50,50)
        self.btnminus.move(130,310)
        self.btnminus.setText("-")
        self.btnminus.clicked.connect(self.btnminus_handler)

        self.btnumn = QtWidgets.QPushButton(self)
        self.btnumn.resize(50,50)
        self.btnumn.move(190,100)
        self.btnumn.setText("*")
        self.btnumn.clicked.connect(self.btnumn_handler)

        self.btndiv = QtWidgets.QPushButton(self)
        self.btndiv.resize(50,50)
        self.btndiv.move(190,170)
        self.btndiv.setText("/")
        self.btndiv.clicked.connect(self.btndiv_handler)

        self.btnanswer = QtWidgets.QPushButton(self)
        self.btnanswer.resize(50,50)
        self.btnanswer.move(190,310)
        self.btnanswer.setText("=")
        self.btnanswer.clicked.connect(self.btnanswer_handler)


    def btn1_handler(self):
        text=self.main_text.text()
        self.main_text.setText(text+"1")

    def btn2_handler(self):
        text=self.main_text.text()
        self.main_text.setText(text+"2")

    def btn3_handler(self):
        text=self.main_text.text()
        self.main_text.setText(text+"3")

    def btn4_handler(self):
        text=self.main_text.text()
        self.main_text.setText(text+"4")

    def btn5_handler(self):
        text=self.main_text.text()
        self.main_text.setText(text+"5")

    def btn6_handler(self):
        text=self.main_text.text()
        self.main_text.setText(text+"6")

    def btn7_handler(self):
        text=self.main_text.text()
        self.main_text.setText(text+"7")

    def btn8_handler(self):
        text=self.main_text.text()
        self.main_text.setText(text+"8")

    def btn9_handler(self):
        text=self.main_text.text()
        self.main_text.setText(text+"9")

    def btn0_handler(self):
        text=self.main_text.text()
        self.main_text.setText(text+"0")

    def btnplus_handler(self):
        text=self.main_text.text()
        self.main_text.setText(text+"+")

    def btnminus_handler(self):
        text=self.main_text.text()
        self.main_text.setText(text+"-")

    def btnumn_handler(self):
        text=self.main_text.text()
        self.main_text.setText(text+"*")

    def btndiv_handler(self):
        text=self.main_text.text()
        self.main_text.setText(text+"/")

    def btnclear_handler(self):
        self.main_text.setText("")

    def btnanswer_handler(self):
        text=self.main_text.text()

        try:
            ans=eval(text)
            self.main_text.setText(str(ans))
        except:
            self.main_text.setText("Неправильный ввод")
    


def application():
    app = QApplication(sys.argv)
    app.setStyleSheet(style_sheet)
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    application()
