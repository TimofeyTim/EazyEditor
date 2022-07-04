from PIL import Image
from PyQt5.QtWidgets import QFileDialog
import os 
from PyQt5.QtGui import QPixmap
from PIL import ImageFilter
from PIL import ImageEnhance 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QInputDialog, QLineEdit,QListWidget,QApplication,QTextEdit, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup)
app = QApplication([])
win = QWidget()
win.resize(700,400)

win.setWindowTitle('Название:Eyse Editor')

K1 = QPushButton('Папка')
K2 = QPushButton('Лево')
K3 = QPushButton('Право')
K4 = QPushButton('Зеркало')
K5 = QPushButton('Резкость')
K6 = QPushButton('Ч/Б')
K7 = QPushButton('Контраст')

papka = ''

okno = QListWidget()

kartinka = QLabel('Картинка демоверсия')

BatonLayto = QHBoxLayout()


BatonLayto.addWidget(K2)
BatonLayto.addWidget(K3)
BatonLayto.addWidget(K4)
BatonLayto.addWidget(K5)
BatonLayto.addWidget(K6)
BatonLayto.addWidget(K7)

v1 =  QVBoxLayout()
v1.addWidget(K1)
v1.addWidget(okno)

v2 = QVBoxLayout()
v2.addWidget(kartinka)
v2.addLayout(BatonLayto)

h1 = QHBoxLayout()
h1.addLayout(v1,1)
h1.addLayout(v2,6)
win.setLayout(h1)

class IMAgessss():
    def __init__(self):
        self.Image = None
        self.papka = None
        self.filename = None
        self.savepapka = 'new/'
    def loadImage(self,filename):
        self.filename = filename
        self.papka = papka
        self.filepath = os.path.join(papka,filename)
        self.Image = Image.open(self.filepath)
    def showimagee(self,path):
        kartinka.hide()
        pix = QPixmap(path)
        pix = pix.scaled(kartinka.width(),kartinka.height(),Qt.KeepAspectRatio)
        kartinka.setPixmap(pix)
        kartinka.show()
    def savephoto(self):
        path = os.path.join(self.papka,self.savepapka)
        if os.path.exists(path) != True or os.path.isdir(path) != True:
            os.mkdir(path)
        path = os.path.join(path,self.filename)
        self.Image.save(path)
    def left(self):
        self.Image = self.Image.transpose(Image.ROTATE_90)
        self.savephoto()
        path = os.path.join(self.papka,self.savepapka,self.filename)
        self.showimagee(path)
    def rezzzkost(self):
        self.Image = self.Image.filter(ImageFilter.SHARPEN)
        self.savephoto()
        path = os.path.join(self.papka,self.savepapka,self.filename)
        self.showimagee(path)
    def right(self):
        self.Image = self.Image.transpose(Image.ROTATE_270)
        self.savephoto()
        path = os.path.join(self.papka,self.savepapka,self.filename)
        self.showimagee(path)
    def zerlako(self):
        self.Image = self.Image.transpose(Image.FLIP_LEFT_RIGHT)
        self.savephoto()
        path = os.path.join(self.papka,self.savepapka,self.filename)
        self.showimagee(path)
    def chb(self):
        self.Image = self.Image.convert('L')
        self.savephoto()
        path = os.path.join(self.papka,self.savepapka,self.filename)
        self.showimagee(path)
    def kontrast(self):
        kontrast = ImageEnhance.Contrast(self.Image)
        self.Image = kontrast.enhance(2)
        self.savephoto()
        path = os.path.join(self.papka,self.savepapka,self.filename)
        self.showimagee(path)
       


curant = IMAgessss()




        
        

def filter(papka):
    exetensens = ['.png','.jpeg','.jpg','.gif']
    try:
        vsefaili = os.listdir(papka)
    except:
        return []
    vsefaili = os.listdir(papka)
    result = []
    
    for element in vsefaili:
        _, file_extension = os.path.splitext(element)
        if file_extension in exetensens:
            result.append(element)
    return result 


def opener():
    global papka 



    papka = QFileDialog.getExistingDirectory()
    result = filter(papka)
    print(result)
    okno.clear()
    okno.addItems(result)


def obr():
    III = okno.selectedItems()[0].text()
    curant.loadImage(III)
    curant.showimagee(curant.filepath)





K1.clicked.connect(opener)
okno.itemClicked.connect(obr)
K2.clicked.connect(curant.left)
K5.clicked.connect(curant.rezzzkost)
K3.clicked.connect(curant.right)
K4.clicked.connect(curant.zerlako)
K6.clicked.connect(curant.chb)
K7.clicked.connect(curant.kontrast)


































win.show()
app.exec()