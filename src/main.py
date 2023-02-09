import sys
from PyQt5 import QtWidgets

from Sticker import Sticker

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    s = Sticker('./src/gif/magenta.gif', xy=[0, 200], size=1, onTop=True)

    sys.exit(app.exec_())