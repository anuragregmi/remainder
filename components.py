from PyQt4.QtCore import Qt

from PyQt4.QtGui import QTextEdit


class TextEdit(QTextEdit):

    def __init__(self, *args):
        super(TextEdit, self).__init__(*args)
        self.keyPressed = None

    def keyPressEvent(self, QKeyEvent):
        self.keyPressed(QKeyEvent)

        if QKeyEvent.key() != Qt.Key_Tab:
            super(TextEdit, self).keyPressEvent(QKeyEvent)

    def setKeyPressHandler(self, method):
        self.keyPressed = method
