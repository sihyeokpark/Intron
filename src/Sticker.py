import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QMovie

class Sticker(QtWidgets.QMainWindow):
    def __init__(self, imgPath, xy, size=1.0, onTop=True):
        super(Sticker, self).__init__()

        self.imgPath = imgPath
        self.xy = xy
        self.size = size
        self.onTop = onTop

        self.setupUi()
        self.show()

    def mouseDoubleClickEvent(self, e):
        QtWidgets.qApp.quit()
    
    def setupUi(self):
        centralWidget = QtWidgets.QWidget(self)
        self.setCentralWidget(centralWidget)

        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint if self.onTop else QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(flags)
        self.setAttribute(QtCore.Qt.WA_NoSystemBackground, True)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

        label = QtWidgets.QLabel(centralWidget)
        movie = QMovie(self.imgPath)
        label.setMovie(movie)
        movie.start()
        movie.stop()

        w = int(movie.frameRect().size().width() * self.size)
        h = int(movie.frameRect().size().height() * self.size)
        movie.setScaledSize(QtCore.QSize(w, h))
        movie.start()

        self.setGeometry(self.xy[0], self.xy[1], w, h)