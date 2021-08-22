
from pprint import pprint as pp
from PyQt5.QtWidgets import QWidget, QGridLayout, QSizePolicy, QLabel
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QFont, QMouseEvent

class UI_TimerWindow(QWidget):
    def __init__(self, current_time="00:00:00", message="Timer Ready"):
        super().__init__()

        layoutGrid = QGridLayout()

        self.setLayout(layoutGrid)
        self.setWindowTitle("Timer Display")

        self.resize(800,600)
        self.setStyleSheet("background-color: Black; color: White;")

        self.timer_display_text = current_time
        self.message_display_text = message
        

        # self.incrincrement = 1.3 # multiplier for text size

        # Timer display setup
        self.timer_text = QLabel()
        self.timer_text.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.timer_text.setText(self.timer_display_text)
        self.timer_text.setAlignment(QtCore.Qt.AlignCenter)
        self.timer_text.resizeEvent = self.resizeTimerText
        layoutGrid.addWidget(self.timer_text)

        # Message disaply setup
        self.message_text = QLabel()
        self.message_text.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.message_text.setText(self.message_display_text)
        self.message_length = (len(self.message_display_text))
        self.message_text.setAlignment(QtCore.Qt.AlignCenter)
        self.message_text.resizeEvent = self.resizeMessageText
        self.message_text.setVisible(False)
        layoutGrid.addWidget(self.message_text)

    def resizeTimerText(self, event):
        
        # print(self.timer_display_text)

        # self.timer_text.setVisible(True)

        increment = 1.65

        self.timer_text_size = int((self.rect().width() / (len(self.timer_display_text))*increment))

        if  self.timer_text_size > 400:
             self.timer_text_size = 400

        # print( self.timer_text_size)

        # font setup
        font = QtGui.QFont()
        font.setPixelSize(self.timer_text_size)
        font.setFamily("Helvetica")
        font.setBold(True)
        self.timer_text.setFont(font)


    def resizeMessageText(self, event):
            
        # print(self.message_display_text)

        self.message_text.setHidden(False)

        increment = 1.5

        self.message_text_size = int((self.rect().width() / (self.message_length)*increment))

        if self.message_text_size > 400:
            self.message_text_size = 400

        print(f"Message length: {self.message_length}, text point size: {self.message_text_size}, window width: {self.rect().width()}")
        # print(self.message_text_size)
        # print(self.rect().width())

        # font setup
        self.font = QtGui.QFont()
        self.font.setPixelSize(self.message_text_size)
        self.font.setFamily("Helvetica")
        self.message_text.setFont(self.font)


    def keyPressEvent(self, e):  
        if e.key() == QtCore.Qt.Key_Escape:
            self.showNormal()
            self.close()

        if e.key() == QtCore.Qt.Key_F:
            if self.isFullScreen():
                self.showNormal()

            else:
                self.showFullScreen()

        if e.key() == QtCore.Qt.Key_M:
            if self.isMaximized():
                self.showNormal()

            else:
                self.showMaximized()
    
    def closeEvent(self, event):
        print("Timer window closed")

    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        event.accept()
        if self.isFullScreen():
            self.showNormal()

        else:
            self.showFullScreen()
    

# def main():
#     app = QApplication(sys.argv)
#     demo = UI_TimerWindow()
#     demo.show()
#     sys.exit(app.exec_())

# main()
