"""A QT widget to create the buttons for the i3Void QT window.
"""

from PyQt5.QtWidgets import QApplication, QColorDialog, QWidget, QPushButton, QHBoxLayout, QVBoxLayout

from PyQt5.QtGui import QColor


class ButtonWidget(QWidget):
    """A QT Widget that:
         1) Instantiates and Styles the "Close" and "Color" buttons
         2) Creates a color picker when the Color button is clicked
    """

    def __init__(self, parent=None):
        """Initialize the buttons, their click event handlers, and their position.
        """

        super(QWidget, self).__init__(parent)
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
        selectedColor = QColorDialog.getColor(color)

        if selectedColor.isValid():
            self._current_color_hex = selectedColor.name()
            self._parent.setWindowColor(self._current_color_hex)
