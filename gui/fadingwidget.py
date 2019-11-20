"""A QT widget to create the buttons for the i3Void QT window.
"""

from PyQt5.QtWidgets import QColorDialog, QWidget, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QColor


class ButtonWidget(QWidget):

    def __init__(self, parent=None):
        """Initialize the buttons, their click event handlers, and their position.
        """

        QWidget.__init__(self, parent)
        self._parent = parent
        self._current_color_hex = "#2e2e2e"

        self.color_button = QPushButton('Color', self)
        self.color_button.clicked.connect(self.showColorPicker)
        self.color_button.resize(self.color_button.sizeHint())

        self.close_button = QPushButton(' X ', self)
        self.close_button.clicked.connect(self._parent.closeWindow)
        self.close_button.resize(self.close_button.sizeHint())

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.color_button)
        hbox.addWidget(self.close_button)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.repaint()

    def showColorPicker(self):
        """Show the color picker when the Color button is clicked.
        """

        color = QColor(0, 0, 0)
        color.setNamedColor(self._current_color_hex)
        selected_color = QColorDialog.getColor(color)

        if selected_color.isValid():
            self._current_color_hex = selected_color.name()
            self._parent.setWindowColor(self._current_color_hex)
