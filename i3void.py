import sys

from PyQt4 import QtGui
from PyQt4 import QtCore

from gui import FadingWidget

class i3Void(QtGui.QMainWindow):

    def __init__(self):
        super(i3Void, self).__init__()

        self.setWindowTitle('i3Void')

        self.fadingButtons = FadingWidget(self)
        self.setCentralWidget(self.fadingButtons)

        self.show()

        self.setWindowColor("#2e2e2e")

        self.installEventFilter(self)

        # Set CTRL+q to exit
        QtGui.QShortcut(QtGui.QKeySequence("Ctrl+Q"), self, self.close)

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.WindowActivate:
            self.fadingButtons.show();
        elif event.type()== QtCore.QEvent.WindowDeactivate:
            self.fadingButtons.hide();
        return QtGui.QWidget.eventFilter(self, source,event)

    def setWindowColor(self, new_color):
        self.setStyleSheet('QMainWindow{background-color: '+new_color+';}')

    def closeWindow(self):
        self.close()
        
    def closeEvent(self, event):
        event.accept()
        
        
def main():

    app = QtGui.QApplication(sys.argv)
    
    sq = i3Void()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
