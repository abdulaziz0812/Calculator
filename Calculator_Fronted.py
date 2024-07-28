from os import system
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel
from PyQt5.QtCore import Qt
system("cls")

app = QApplication([])

oyna = QWidget()
oyna.setWindowTitle("Calculator")
oyna.move(1000, 200)
oyna.setFixedSize(340, 560)

input1 = QLineEdit(oyna)
input1.setGeometry(1, 170, 340, 90)
input1.setStyleSheet("""font-size: 30px;""")
input1.setAlignment(Qt.AlignRight)

botton1 = QPushButton("C", oyna)
botton1.setGeometry(1, 260, 90, 65)
botton1.setStyleSheet("""
    font-size: 20px;
    color: red;
""")
botton2 = QPushButton("(", oyna)
botton2.setGeometry(85, 260, 50, 65)
botton2.setStyleSheet("""
    font-size: 20px;
    color: blue;                      
""")
botton_2 = QPushButton(")", oyna)
botton_2.setGeometry(125, 260, 50, 65)
botton_2.setStyleSheet("""
    font-size: 20px;
    color: blue;                      
""")
botton3 = QPushButton("↩", oyna)
botton3.setGeometry(170, 260, 90, 65)
botton3.setStyleSheet("""
    font-size: 30px;
    color: blue;
    """)
botton4 = QPushButton("/", oyna)
botton4.setGeometry(255, 260, 90, 65)
botton4.setStyleSheet("""
    font-size: 20px;
    color: blue;
    """)
botton5 = QPushButton("7", oyna)
botton5.setGeometry(1, 320, 90, 65)
botton5.setStyleSheet("""
    font-size: 20px;
    """)
botton6 = QPushButton("8", oyna)
botton6.setGeometry(85, 320, 90, 65)
botton6.setStyleSheet("""
    font-size: 20px;
    """)
botton7 = QPushButton("9", oyna)
botton7.setGeometry(170, 320, 90, 65)
botton7.setStyleSheet("""
    font-size: 20px;
    """)
botton8 = QPushButton("*", oyna)
botton8.setGeometry(255, 320, 90, 65)
botton8.setStyleSheet("""
    font-size: 20px;
    color: blue;
    """)
botton9 = QPushButton("4", oyna)
botton9.setGeometry(1, 380, 90, 65)
botton9.setStyleSheet("""
    font-size: 20px;
    """)
botton10 = QPushButton("5", oyna)
botton10.setGeometry(85, 380, 90, 65)
botton10.setStyleSheet("""
    font-size: 20px;
    """)
botton11 = QPushButton("6", oyna)
botton11.setGeometry(170, 380, 90, 65)
botton11.setStyleSheet("""
    font-size: 20px;
    """)
botton12 = QPushButton("-", oyna)
botton12.setGeometry(255, 380, 90, 65)
botton12.setStyleSheet("""
    font-size: 30px;
    color: blue;
    """)
botton13 = QPushButton("1", oyna)
botton13.setGeometry(1, 440, 90, 65)
botton13.setStyleSheet("""
    font-size: 20px;
    """)
botton14 = QPushButton("2", oyna)
botton14.setGeometry(85, 440, 90, 65)
botton14.setStyleSheet("""
    font-size: 20px;
    """)
botton15 = QPushButton("3", oyna)
botton15.setGeometry(170, 440, 90, 65)
botton15.setStyleSheet("""
    font-size: 20px;
    """)
botton16 = QPushButton("+", oyna)
botton16.setGeometry(255, 440, 90, 65)
botton16.setStyleSheet("""
    font-size: 20px;
    color: blue;
    """)
botton17 = QPushButton("%", oyna)
botton17.setGeometry(1, 500, 90, 65)
botton17.setStyleSheet("""
    font-size: 20px;
    """)
botton18 = QPushButton("0", oyna)
botton18.setGeometry(85, 500, 90, 65)
botton18.setStyleSheet("""
    font-size: 20px;
    """)
botton19 = QPushButton(".", oyna)
botton19.setGeometry(170, 500, 90, 65)
botton19.setStyleSheet("""
    font-size: 20px;
    """)
botton20 = QPushButton("=", oyna)
botton20.setGeometry(255, 500, 90, 65)
botton20.setStyleSheet("""
    font-size: 30px;
    color: white;
    background-color: blue;
    """)
hisoblandi = False 

def input_func(text):
    global hisoblandi
    global malumot
    if hisoblandi:
        input1.clear()
        hisoblandi = False
    input1.setText(input1.text() + text)
    malumot.clear()

def belgi_qoshish(belgi):
    global hisoblandi
    oxirgi_belgi = input1.text()[-1:] if input1.text() else ""
    if hisoblandi:
        hisoblandi = False
    if oxirgi_belgi not in "+-*/":
        input1.setText(input1.text() + belgi)

def belgi1():
    global hisoblandi
    if hisoblandi:
        input1.clear()
        hisoblandi = False
    input1.setText(input1.text() + "(")
        
def belgi2():
    global hisoblandi
    if hisoblandi:
        input1.clear()
        hisoblandi = False
    input1.setText(input1.text() + ")")

def belgi3():
    global hisoblandi
    if hisoblandi:
        input1.clear()
        hisoblandi = False
    if '.' not in input1.text()[-1:]:
        input1.setText(input1.text() + ".")
    
def bitta_uchir():
    input1.setText(input1.text()[:-1])
    
malumot = QLabel(oyna)
malumot.setStyleSheet("""
    font-size: 20px;
    color: red;                  
    """)

def hisoblash():
    global hisoblandi
    try:
        natija = input1.text().replace('%', '/100')
        result = eval(natija)
        input1.setText(str(result))
        hisoblandi = True 
    except ZeroDivisionError:
        malumot.setText("0 ga bo'lib bo'lmaydi")
        malumot.adjustSize()
        input1.clear()
    except:
        malumot.setText("Xato amal")
        malumot.adjustSize()
        input1.clear()


botton1.clicked.connect(lambda: input1.clear())
botton2.clicked.connect(belgi1)
botton_2.clicked.connect(belgi2)
botton3.clicked.connect(bitta_uchir)
botton4.clicked.connect(lambda: belgi_qoshish("/"))
botton5.clicked.connect(lambda: input_func("7"))
botton6.clicked.connect(lambda: input_func("8"))
botton7.clicked.connect(lambda: input_func("9"))
botton8.clicked.connect(lambda: belgi_qoshish("*"))
botton9.clicked.connect(lambda: input_func("4"))
botton10.clicked.connect(lambda: input_func("5"))
botton11.clicked.connect(lambda: input_func("6"))
botton12.clicked.connect(lambda: belgi_qoshish("-"))
botton13.clicked.connect(lambda: input_func("1"))
botton14.clicked.connect(lambda: input_func("2"))
botton15.clicked.connect(lambda: input_func("3"))
botton16.clicked.connect(lambda: belgi_qoshish("+"))
botton17.clicked.connect(lambda: belgi_qoshish("%"))
botton18.clicked.connect(lambda: input_func("0"))
botton19.clicked.connect(belgi3)
botton20.clicked.connect(hisoblash)

oyna.show()
app.exec_()
