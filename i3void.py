#!/usr/bin/env python

"""i3Void provides a blank window to pad a workspace in 
the i3 window manager.

"""

__author__ = "Destin Moulton"
__email__ = "destin.moulton@gmail.com"
__copyright__ = "Copyright 2016, Destin Moulton"
__license__ = "MIT"
__status__ = "Development"
__version__ = "0.2.0"

import sys

from PyQt5.QtCore import QEvent
from PyQt5.QtGui import QKeySequence

from PyQt5.QtWidgets import QApplication, QMainWindow, QShortcut, QWidget

from gui.buttonwidget import ButtonWidget


class i3Void(QMainWindow):
    """Create the QT window application.
    """

    def __init__(self):
        """Set the parameters for the QT window.
        """

        #super(i3Void, self).__init__()
        QMainWindow.__init__(self)

        self.setWindowTitle('i3Void')

        self.buttonWidget = ButtonWidget(self)
        self.setCentralWidget(self.buttonWidget)

        self.show()

        self.setWindowColor("#2e2e2e")

        self.installEventFilter(self)

        # Setup Ctrl+q to exit
        QShortcut(QKeySequence("Ctrl+Q"), self, self.close)

    def eventFilter(self, source, event):
        """Hide and show the buttons when the window is focused.
        """

        if event.type() == QEvent.WindowActivate:
            self.buttonWidget.show()
        elif event.type() == QEvent.WindowDeactivate:
            self.buttonWidget.hide()
        return QWidget.eventFilter(self, source, event)

    def setWindowColor(self, new_color):
        """Change the color of the window.
        """

        self.setStyleSheet('QMainWindow{background-color: '+new_color+';}')

    def closeWindow(self):
        """Close the window.
        """

        self.close()

    def closeEvent(self, event):
        """Accept a close event.
        """

        event.accept()


if __name__ == '__main__':
    """Start the window when this script is run.
    """

    # Pass any args to the QT application
    app = QApplication(sys.argv)

    # Instantiate the i3Void window
    sq = i3Void()

    # Run the app
    sys.exit(app.exec_())
