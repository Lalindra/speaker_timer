from timergui5 import Ui_controlWindow
from timerwindow2 import UI_TimerWindow
from help import Ui_Dialog

import sys
import json
from PyQt5 import QtWidgets, QtGui, QtCore

class MasterTimer(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # creating instance for referencing
        self.ui = Ui_controlWindow()
        self.ui.setupUi(self)

        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap("pt_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        #initialise timer
        self.remaining_seconds = 600 # Initial display value
        self.timer_is_active = False # Setting state of timer to not active

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.displayTime)

        # initialising message
        self.display_message = self.ui.txtMessageBox.text()

        # disabling buttons
        self.ui.btnPause.setEnabled(False)
        self.ui.btnStop.setEnabled(False)

        # Hiding the message label at the start
        self.ui.lblMessageDisplay.setVisible(False)

        # Initialising the Timer Display Window
        self.current_time = self.ui.lblTimeDisplay.text()
        self.message = self.ui.txtMessageBox.text()
        self.app = QtWidgets.QWidget()
        self.ui2 = UI_TimerWindow(self.current_time, self.message)

        # Menu triggers
        self.ui.actionLoad_Settings.triggered.connect(self.loadSettings)
        self.ui.actionSave_Settings.triggered.connect(self.saveSettings)
        self.ui.actionExit.triggered.connect(self.exit)
        self.ui.actionWindow_mode.triggered.connect(lambda state:self.timerDisplayWindow(1))
        self.ui.actionFullscreen.triggered.connect(lambda state:self.timerDisplayWindow(2))
        self.ui.actionClose_Window.triggered.connect(self.closeTimerDisplayWindow)
        self.ui.actionInteface_Help.triggered.connect(self.showHelp)
        self.ui.actionAbout.triggered.connect(self.about)
    
        # Button triggers
        self.ui.btnSetTime.clicked.connect(self.setDuration)
        self.ui.btnResetTime.clicked.connect(self.resetDuration)
        self.ui.btnShowMessage.clicked.connect(self.showMessage)
        self.ui.btnHideMessage.clicked.connect(self.hideMessage)

        self.ui.btnStart.clicked.connect(self.start)
        self.ui.btnPause.clicked.connect(self.pause)
        self.ui.btnStop.clicked.connect(self.stop)
        

    # Methods are deployed from here

    # Time calculation and display funtion

    def displayTime(self):

        if self.remaining_seconds > 0:
    
            self.remaining_seconds -= 1

            h = self.remaining_seconds // 3600
            m = (self.remaining_seconds // 60)
            
            if m <= 0:
                m = 0
            elif m > 60:
                m = m - 60 * h
            s = self.remaining_seconds % 60

            timer = "{:02d}:{:02d}:{:02d}".format(h,m, s)
            self.ui.lblTimeDisplay.setText(str(timer))
            if self.ui2.isVisible():
                self.ui2.timer_text.setText(str(timer)) # Timer Display Window

            # Progress bar
            progress_bar_value = (self.remaining_seconds/ self.total_seconds)*100
            self.ui.progressBar.setProperty("value", progress_bar_value)

            # Check timer 
            print(timer, end="\r")
           
        else: 
            self.timer_window_state("alert") # Specifying to display as an ALERT!"
            self.stop()
            

    # Menu functions

    def loadSettings(self):
        
        file_name = "settings.json"

        with open(file_name) as file_contents:
            load_data = file_contents.read()

        print(type(load_data))
        print(load_data)

        data = json.loads(load_data)

        self.ui.txtMessageBox.setText(data["message"])        
        self.ui.spinHrs.setValue(int(data["hours"]))
        self.ui.spinMins.setValue(int(data["minutes"]))
        self.ui.spinSecs.setValue(int(data["seconds"]))
        self.setDuration()

    def saveSettings(self):
        save_data = {"message" : self.ui.txtMessageBox.text(), "hours" : self.ui.spinHrs.text(), "minutes" :self.ui.spinMins.text(), "seconds" : self.ui.spinSecs.text()}
        print(save_data)

        # Serialize data into file:
        json.dump(save_data, open( "settings.json", 'w' ) )
        
    def exit(self):

        if self.timer_is_active:
            msg = QtWidgets.QMessageBox()
            msg.setWindowIcon(self.icon)
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setWindowTitle("WARNING - Timer Active.")
            msg.setText("Timer is still running!")
            msg.setInformativeText("Are you sure you want to close the application?")
            msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
       
            returnVal = msg.exec_()
            print ("value of pressed message box button:", returnVal)

            if returnVal == 16384:
                self.timer.stop()
                sys.exit(app.exec_())

            else:
                self.cleared_to_close = False
        
        else:
            self.timer.stop()
            sys.exit(app.exec_())


    # Bring up the timer display window
    def timerDisplayWindow(self, state):

        if state == 1 and self.ui2.isVisible() == False: # select between windowed and fullscreen
            print(self.ui2.isVisible())
            self.ui2.show()
            
        elif state == 2 and self.ui2.isVisible() == False:
            print(self.ui2.isVisible())
            self.ui2.showFullScreen()

        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowIcon(self.icon)
            msg.setWindowTitle("Redundant action")
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Timer window is already launched!")
            msg.setStandardButtons(QtWidgets.QMessageBox.Close)
            returnVal = msg.exec_()
            
    def closeTimerDisplayWindow(self):

        if self.timer_is_active:
            msg = QtWidgets.QMessageBox()
            msg.setWindowIcon(self.icon)
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setWindowTitle("Warning!!! Timer Active!!!")
            msg.setText("Timer is still running. Are you sure you want to close the display window?")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.No)
            returnVal = msg.exec_()
        
            if returnVal == 1024:
                self.ui2.close()
                self.timer_window_is_open = False
              
        else:
            self.ui2.close()
            self.timer_window_is_open = False

    def showHelp(self):
        
        help_dialog = QtWidgets.QDialog()
        self.d = Ui_Dialog()
        self.d.setupUi(help_dialog)
        help_dialog.setWindowIcon(self.icon)
        help_dialog.exec_()
        
        # Code for hiding the ? icon in the help window. This should be implemented in the UI_Dialog
        # Dialog.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
        
    def about(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowIcon(self.icon)
        msg.setWindowTitle("Presenter Timer - version 0.4")
        msg.setText("Created by Lalindra Amarasekara")
        msg.setInformativeText("Free to use and distribute")
        msg.setDetailedText("Share freely and send your comments to lalindra@cyberillusions.co")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        
        returnVal = msg.exec_()
        print ("value of pressed message box button:", returnVal)

    def setDuration(self):
        _hrs = int(self.ui.spinHrs.text())
        _mins = int(self.ui.spinMins.text())
        _secs = int(self.ui.spinSecs.text())

        self.remaining_seconds = int((_hrs*3600) + (_mins*60) + _secs) # total time set for the timer
        self.showtime = "{:02d}:{:02d}:{:02d}".format(_hrs, _mins, _secs)

        # printing to check variables
        print(self.showtime)
        print(f"Total seconds: {self.remaining_seconds}")

        self.timer_window_state(None)
        self.ui.lblTimeDisplay.setText(self.showtime)
        self.ui.lblMessageDisplay.setVisible(False)
    
        if self.ui2.isVisible():
            self.ui2.timer_text.setText(self.showtime)
            self.ui2.message_text.setVisible(False)
            self.ui2.timer_text.setVisible(True)

    def resetDuration(self):
        self.ui.spinHrs.setProperty("value", 0)
        self.ui.spinMins.setProperty("value", 0)
        self.ui.spinSecs.setProperty("value", 0)

        self.setDuration()
        self.ui2.timer_text.setVisible(True)

        self.ui.progressBar.setProperty("value", 0)

    def showMessage(self):

        self.display_message = self.ui.txtMessageBox.text()

        text_size = 48 - len(self.display_message)

        if len(self.display_message) == 0:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setWindowTitle("Error")
            msg.setText("Nothing to Show. Please type a message")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            returnVal = msg.exec_()
            
        else:
            font = QtGui.QFont()
            self.ui.lblMessageDisplay.setVisible(True)
            font.setPointSize(text_size)
            font.setBold(False)
            font.setItalic(False)
            font.setWeight(50)
            self.ui.lblMessageDisplay.setFont(font)
            self.ui.lblMessageDisplay.setText(self.display_message)

            # if self.timer_window_is_open:
            if self.ui2.isVisible():
                
                self.ui2.timer_text.setVisible(False)
                self.ui2.resizeMessageText(None)
                self.ui2.message_text.setVisible(True)
                self.ui2.message_text.setText(self.display_message)
                self.ui2.message_length = (len(self.display_message))
                self.ui2.resizeMessageText(None)
                print(self.ui2.isVisible())
            
    def hideMessage(self):
        self.timer_window_state(None)
        self.ui.lblMessageDisplay.setVisible(False) 
        if self.ui2.isVisible():
            self.ui2.message_text.setVisible(False)
            self.ui2.timer_text.setVisible(True)

    def start(self, seconds):

        self.timer_window_state(None)
        if self.timer_is_active == False:
            self.setDuration()
            
        self.timer_is_active = True
        self.total_seconds = self.remaining_seconds
        self.timer.start(1000)
        self.ui.btnStart.setText("Start")
        self.ui.btnStart.setEnabled(False)
        self.ui.btnPause.setEnabled(True)
        self.ui.btnStop.setEnabled(True)
        self.ui.lblMessageDisplay.setVisible(False)
        self.ui2.timer_text.setVisible(True)

    def pause(self):
        self.timer.stop() # in QTimer stop means pause.
        self.ui.btnStart.setEnabled(True)
        self.ui.btnStart.setText("Continue")
        self.ui.btnPause.setEnabled(False)

    def stop(self):
        self.timer.stop()
        self.timer_is_active = False
        self.ui.btnStart.setEnabled(True)
        self.ui.btnPause.setEnabled(False)
        self.ui.btnStop.setEnabled(False)
        self.ui.btnStart.setText("Start")

        self.display_message = self.ui.txtMessageBox.text()
        if len(self.display_message) != 0:
            self.showMessage()

        # self.setDuration()

    def closeEvent(self, event):
        
        self.exit()
        
        if self.cleared_to_close:
            event.accept()

        else:
            self.cleared_to_close = False
            event.ignore()

        print("Control window closed")


    def timer_window_state(self, style=None):

        if style == "alert":
            self.ui2.setStyleSheet("background-color: Red; color: White")
            print("Red")
        else:
            self.ui2.setStyleSheet("background-color: Black; color: White")
            print("Black")


if __name__ == '__main__':
    
    app = QtWidgets.QApplication(sys.argv)
    main_app = MasterTimer()
    main_app.show()
    app.exec_()
