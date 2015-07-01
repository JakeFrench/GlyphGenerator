__author__ = 'Dr Jake French'
import sys
from PyQt4 import QtGui, QtCore
from userInterface import Ui_MatrixToHex


class Interface(QtGui.QMainWindow):
    def __init__(self):
        # Initialise GUI
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MatrixToHex()
        self.ui.setupUi(self)
        self.data = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        self.Btns = {'aa': (7,1), 'ab': (7,2), 'ac': (7,4), 'ad': (7,8), 'ae': (7,16), 'af': (7,32), 'ag': (7,64), 'ah': (7,128),\
                     'ba': (6,1), 'bb': (6,2), 'bc': (6,4), 'bd': (6,8), 'be': (6,16), 'bf': (6,32), 'bg': (6,64), 'bh': (6,128),\
                     'ca': (5,1), 'cb': (5,2), 'cc': (5,4), 'cd': (5,8), 'ce': (5,16), 'cf': (5,32), 'cg': (5,64), 'ch': (5,128),\
                     'da': (4,1), 'db': (4,2), 'dc': (4,4), 'dd': (4,8), 'de': (4,16), 'df': (4,32), 'dg': (4,64), 'dh': (4,128),\
                     'ea': (3,1), 'eb': (3,2), 'ec': (3,4), 'ed': (3,8), 'ee': (3,16), 'ef': (3,32), 'eg': (3,64), 'eh': (3,128),\
                     'fa': (2,1), 'fb': (2,2), 'fc': (2,4), 'fd': (2,8), 'fe': (2,16), 'ff': (2,32), 'fg': (2,64), 'fh': (2,128),\
                     'ga': (1,1), 'gb': (1,2), 'gc': (1,4), 'gd': (1,8), 'ge': (1,16), 'gf': (1,32), 'gg': (1,64), 'gh': (1,128),\
                     'ha': (0,1), 'hb': (0,2), 'hc': (0,4), 'hd': (0,8), 'he': (0,16), 'hf': (0,32), 'hg': (0,64), 'hh': (0,128)}
        for eachBtn in self.Btns.keys():
            eval('''self.ui.''' + eachBtn + '''.setCheckable(True)''')
            eval('''self.ui.''' + eachBtn + '''.toggled.connect(self.onPlot)''')
        #self.onClear()

    def onClear(self):
        for eachBtn in self.Btns:
            eval('''self.ui.''' + eachBtn + '''.setStyleSheet('background: 240')''')
        self.data = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        self.onPrint()

    def onPlot(self, checked):
        # define data
        source_button = str(self.sender().objectName())
        column, value = self.Btns[source_button]
        # establish which button was pressed
        if eval('''self.ui.''' + source_button + '''.isChecked()''') == True:
            eval('''self.ui.''' + source_button + '''.setStyleSheet('background: red')''')
            self.data[column] += value
        else:
            eval('''self.ui.''' + source_button + '''.setStyleSheet('background: 240')''')
            self.data[column] -= value
        self.onPrint()

    def onPrint(self):
        text = ''
        for each in self.data:
            text += '0x' + format(each, '02x') + ' '
        self.ui.screen.setText(text)

if __name__ == '__main__':
    app  = QtGui.QApplication(sys.argv)
    app.setStyle(QtGui.QStyleFactory.create("plastique"))
    main = Interface()
    main.show()
    sys.exit(app.exec_())
