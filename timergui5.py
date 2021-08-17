# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timergui5.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_controlWindow(object):
    def setupUi(self, controlWindow):
        controlWindow.setObjectName("controlWindow")
        controlWindow.setEnabled(True)
        controlWindow.resize(473, 397)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(controlWindow.sizePolicy().hasHeightForWidth())
        controlWindow.setSizePolicy(sizePolicy)
        controlWindow.setMinimumSize(QtCore.QSize(473, 397))
        controlWindow.setMaximumSize(QtCore.QSize(473, 397))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pt_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        controlWindow.setWindowIcon(icon)
        controlWindow.setWindowOpacity(1.0)
        controlWindow.setAutoFillBackground(False)
        controlWindow.setStyleSheet("QMainWindow {\n"
"    background-color: rgb(36, 42, 44);\n"
"}\n"
"\n"
"QStatusBar {\n"
"     color: rgb(186, 189, 182);\n"
"}\n"
"\n"
"QMenuBar {\n"
"          color: rgb(186, 189, 182);\n"
"             background-color: rgb(36, 42, 44);\n"
"           border: 1px solid ;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"         color: rgb(186, 189, 182);\n"
"            background-color: rgb(36, 42, 44);\n"
"}\n"
"\n"
"QMenuBar::item::selected {\n"
"            background-color: rgb(30,30,30);\n"
"}\n"
"\n"
"QMenu {\n"
"           color: rgb(186, 189, 182);\n"
"                background-color: rgb(36, 42, 44);\n"
"            border: 1px solid ;\n"
"}\n"
"\n"
"QMenu::item::selected {\n"
"            background-color: rgb(30,30,30);\n"
"\n"
"}")
        controlWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        controlWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(controlWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(36, 42, 44);\n"
"color: rgb(142, 142, 143);\n"
"border-color: rgb(238, 238, 236);")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 15, 451, 131))
        self.frame.setStyleSheet("border-color: rgb(238, 238, 236);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(7)
        self.frame.setMidLineWidth(3)
        self.frame.setObjectName("frame")
        self.lblTimeDisplay = QtWidgets.QLabel(self.frame)
        self.lblTimeDisplay.setGeometry(QtCore.QRect(10, 10, 431, 101))
        font = QtGui.QFont()
        font.setPointSize(69)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lblTimeDisplay.setFont(font)
        self.lblTimeDisplay.setAutoFillBackground(False)
        self.lblTimeDisplay.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(211, 215, 207);\n"
"")
        self.lblTimeDisplay.setMidLineWidth(3)
        self.lblTimeDisplay.setTextFormat(QtCore.Qt.PlainText)
        self.lblTimeDisplay.setScaledContents(False)
        self.lblTimeDisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTimeDisplay.setObjectName("lblTimeDisplay")
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(10, 115, 431, 6))
        self.progressBar.setStyleSheet("QProgressBar\n"
"{\n"
"    background-color: rgb(55, 55, 55);\n"
"    border: black;\n"
"    border-radius: 1px;\n"
"\n"
"}\n"
"QProgressBar::chunk \n"
"{\n"
"\n"
"    background-color: rgb(95, 95, 95);\n"
"    border-radius :15px;\n"
"} ")
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", 100)
        self.progressBar.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(True)
        self.progressBar.setObjectName("progressBar")
        self.lblMessageDisplay = QtWidgets.QLabel(self.frame)
        self.lblMessageDisplay.setEnabled(True)
        self.lblMessageDisplay.setGeometry(QtCore.QRect(10, 10, 431, 101))
        font = QtGui.QFont()
        font.setPointSize(69)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lblMessageDisplay.setFont(font)
        self.lblMessageDisplay.setAutoFillBackground(False)
        self.lblMessageDisplay.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(211, 215, 207);\n"
"")
        self.lblMessageDisplay.setMidLineWidth(3)
        self.lblMessageDisplay.setTextFormat(QtCore.Qt.PlainText)
        self.lblMessageDisplay.setScaledContents(False)
        self.lblMessageDisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMessageDisplay.setObjectName("lblMessageDisplay")
        self.mainButtonFrame = QtWidgets.QFrame(self.centralwidget)
        self.mainButtonFrame.setGeometry(QtCore.QRect(10, 155, 451, 91))
        self.mainButtonFrame.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.mainButtonFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainButtonFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainButtonFrame.setObjectName("mainButtonFrame")
        self.widget = QtWidgets.QWidget(self.mainButtonFrame)
        self.widget.setGeometry(QtCore.QRect(0, 0, 451, 91))
        self.widget.setStyleSheet("background-color: rgba(0, 0, 0,0);\n"
"border-color: rgb(0, 0, 0);\n"
"border-width: 1px")
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnStart = QtWidgets.QPushButton(self.widget)
        self.btnStart.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnStart.sizePolicy().hasHeightForWidth())
        self.btnStart.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnStart.setFont(font)
        self.btnStart.setStatusTip("")
        self.btnStart.setStyleSheet("QPushButton {\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(0,153,77);\n"
"    border-style: outset;\n"
"     border-radius: 10px;\n"
"    border-width: 1px;\n"
"    border-color: rgb(46, 52, 54);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0,162,55);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0,173,77);\n"
"}\n"
"\n"
"\n"
"QPushButton:disabled {\n"
"    color: rgb(50, 50, 50);\n"
"    background-color: rgb(50, 100, 74);\n"
"}")
        self.btnStart.setObjectName("btnStart")
        self.horizontalLayout.addWidget(self.btnStart)
        self.btnPause = QtWidgets.QPushButton(self.widget)
        self.btnPause.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPause.sizePolicy().hasHeightForWidth())
        self.btnPause.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnPause.setFont(font)
        self.btnPause.setStyleSheet("QPushButton {\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(179,119,0);\n"
"    border-style: outset;\n"
"     border-radius: 10px;\n"
"    border-width: 1px;\n"
"    border-color: rgb(46, 52, 54);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(179,100,0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(179,139,0);\n"
"}\n"
"\n"
"\n"
"QPushButton:disabled {\n"
"    color: rgb(50, 50, 50);\n"
"    background-color: rgb(150,80,0);\n"
"}\n"
"\n"
"\n"
"")
        self.btnPause.setObjectName("btnPause")
        self.horizontalLayout.addWidget(self.btnPause)
        self.btnStop = QtWidgets.QPushButton(self.widget)
        self.btnStop.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnStop.sizePolicy().hasHeightForWidth())
        self.btnStop.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnStop.setFont(font)
        self.btnStop.setStatusTip("")
        self.btnStop.setWhatsThis("")
        self.btnStop.setStyleSheet("QPushButton {\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(179,30,0);\n"
"    border-style: outset;\n"
"     border-radius: 10px;\n"
"    border-width: 1px;\n"
"    border-color: rgb(46, 52, 54);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    \n"
"    background-color: rgb(162,30,0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    \n"
"    background-color: rgb(195,30,0);\n"
"}\n"
"\n"
"\n"
"QPushButton:disabled {\n"
"    color: rgb(50, 50, 50);\n"
"    background-color: rgb(142,10,0);\n"
"}\n"
"\n"
"\n"
"")
        self.btnStop.setObjectName("btnStop")
        self.horizontalLayout.addWidget(self.btnStop)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(10, 255, 451, 91))
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.lblEndMessage = QtWidgets.QLabel(self.frame_3)
        self.lblEndMessage.setGeometry(QtCore.QRect(10, 62, 61, 17))
        self.lblEndMessage.setObjectName("lblEndMessage")
        self.txtMessageBox = QtWidgets.QLineEdit(self.frame_3)
        self.txtMessageBox.setGeometry(QtCore.QRect(79, 58, 241, 25))
        self.txtMessageBox.setStyleSheet("/* background-color: rgb(60, 60, 60); */\n"
"\n"
"background-color: rgb(32, 32, 32);\n"
"border-color: rgb(65, 67, 63);\n"
"border-style: inset;\n"
"border-width: 1px;\n"
"")
        self.txtMessageBox.setMaxLength(26)
        self.txtMessageBox.setObjectName("txtMessageBox")
        self.btnSetTime = QtWidgets.QPushButton(self.frame_3)
        self.btnSetTime.setGeometry(QtCore.QRect(330, 25, 51, 25))
        self.btnSetTime.setObjectName("btnSetTime")
        self.btnShowMessage = QtWidgets.QPushButton(self.frame_3)
        self.btnShowMessage.setGeometry(QtCore.QRect(330, 58, 51, 25))
        self.btnShowMessage.setObjectName("btnShowMessage")
        self.spinSecs = QtWidgets.QSpinBox(self.frame_3)
        self.spinSecs.setGeometry(QtCore.QRect(262, 25, 57, 26))
        self.spinSecs.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spinSecs.setMaximum(59)
        self.spinSecs.setObjectName("spinSecs")
        self.lbsCountDownTime = QtWidgets.QLabel(self.frame_3)
        self.lbsCountDownTime.setGeometry(QtCore.QRect(10, 25, 131, 26))
        self.lbsCountDownTime.setObjectName("lbsCountDownTime")
        self.spinMins = QtWidgets.QSpinBox(self.frame_3)
        self.spinMins.setGeometry(QtCore.QRect(201, 25, 57, 26))
        self.spinMins.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spinMins.setMaximum(59)
        self.spinMins.setProperty("value", 10)
        self.spinMins.setObjectName("spinMins")
        self.spinHrs = QtWidgets.QSpinBox(self.frame_3)
        self.spinHrs.setGeometry(QtCore.QRect(140, 25, 57, 26))
        self.spinHrs.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spinHrs.setMaximum(59)
        self.spinHrs.setObjectName("spinHrs")
        self.lblHours = QtWidgets.QLabel(self.frame_3)
        self.lblHours.setGeometry(QtCore.QRect(140, 9, 51, 17))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblHours.setFont(font)
        self.lblHours.setObjectName("lblHours")
        self.lbsMinutes = QtWidgets.QLabel(self.frame_3)
        self.lbsMinutes.setGeometry(QtCore.QRect(200, 9, 51, 17))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbsMinutes.setFont(font)
        self.lbsMinutes.setObjectName("lbsMinutes")
        self.lbsSeconds = QtWidgets.QLabel(self.frame_3)
        self.lbsSeconds.setGeometry(QtCore.QRect(262, 9, 51, 17))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbsSeconds.setFont(font)
        self.lbsSeconds.setObjectName("lbsSeconds")
        self.btnResetTime = QtWidgets.QPushButton(self.frame_3)
        self.btnResetTime.setGeometry(QtCore.QRect(390, 25, 51, 25))
        self.btnResetTime.setObjectName("btnResetTime")
        self.btnHideMessage = QtWidgets.QPushButton(self.frame_3)
        self.btnHideMessage.setGeometry(QtCore.QRect(390, 58, 51, 25))
        self.btnHideMessage.setObjectName("btnHideMessage")
        controlWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(controlWindow)
        self.statusbar.setObjectName("statusbar")
        controlWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(controlWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 473, 23))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuTimer_Display = QtWidgets.QMenu(self.menubar)
        self.menuTimer_Display.setObjectName("menuTimer_Display")
        self.menuOpen_Window = QtWidgets.QMenu(self.menuTimer_Display)
        self.menuOpen_Window.setObjectName("menuOpen_Window")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        controlWindow.setMenuBar(self.menubar)
        self.actionLoad_Settings = QtWidgets.QAction(controlWindow)
        self.actionLoad_Settings.setObjectName("actionLoad_Settings")
        self.actionSave_Settings = QtWidgets.QAction(controlWindow)
        self.actionSave_Settings.setObjectName("actionSave_Settings")
        self.actionExit = QtWidgets.QAction(controlWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionLaunch_in_Fullscreen = QtWidgets.QAction(controlWindow)
        self.actionLaunch_in_Fullscreen.setObjectName("actionLaunch_in_Fullscreen")
        self.actionInteface_Help = QtWidgets.QAction(controlWindow)
        self.actionInteface_Help.setObjectName("actionInteface_Help")
        self.actionAbout = QtWidgets.QAction(controlWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionFullscreen = QtWidgets.QAction(controlWindow)
        self.actionFullscreen.setObjectName("actionFullscreen")
        self.actionWindow_mode = QtWidgets.QAction(controlWindow)
        self.actionWindow_mode.setObjectName("actionWindow_mode")
        self.actionClose_Window = QtWidgets.QAction(controlWindow)
        self.actionClose_Window.setObjectName("actionClose_Window")
        self.menuSettings.addAction(self.actionLoad_Settings)
        self.menuSettings.addAction(self.actionSave_Settings)
        self.menuSettings.addAction(self.actionExit)
        self.menuOpen_Window.addAction(self.actionFullscreen)
        self.menuOpen_Window.addAction(self.actionWindow_mode)
        self.menuTimer_Display.addAction(self.menuOpen_Window.menuAction())
        self.menuTimer_Display.addAction(self.actionClose_Window)
        self.menuHelp.addSeparator()
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionInteface_Help)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuTimer_Display.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(controlWindow)
        QtCore.QMetaObject.connectSlotsByName(controlWindow)
        controlWindow.setTabOrder(self.btnStart, self.btnPause)
        controlWindow.setTabOrder(self.btnPause, self.btnStop)
        controlWindow.setTabOrder(self.btnStop, self.spinHrs)
        controlWindow.setTabOrder(self.spinHrs, self.spinMins)
        controlWindow.setTabOrder(self.spinMins, self.spinSecs)
        controlWindow.setTabOrder(self.spinSecs, self.btnSetTime)
        controlWindow.setTabOrder(self.btnSetTime, self.btnResetTime)
        controlWindow.setTabOrder(self.btnResetTime, self.txtMessageBox)
        controlWindow.setTabOrder(self.txtMessageBox, self.btnShowMessage)
        controlWindow.setTabOrder(self.btnShowMessage, self.btnHideMessage)

    def retranslateUi(self, controlWindow):
        _translate = QtCore.QCoreApplication.translate
        controlWindow.setWindowTitle(_translate("controlWindow", "Presentation Timer"))
        controlWindow.setWhatsThis(_translate("controlWindow", "Simpler Presentation Timer v.1.0"))
        self.lblTimeDisplay.setText(_translate("controlWindow", "00:10:00"))
        self.progressBar.setToolTip(_translate("controlWindow", "Progress of time remaining"))
        self.lblMessageDisplay.setText(_translate("controlWindow", "Message"))
        self.btnStart.setToolTip(_translate("controlWindow", "Start timer"))
        self.btnStart.setText(_translate("controlWindow", "Start"))
        self.btnPause.setToolTip(_translate("controlWindow", "Pause at current time"))
        self.btnPause.setText(_translate("controlWindow", "Pause"))
        self.btnStop.setToolTip(_translate("controlWindow", "Stop timer and show end message"))
        self.btnStop.setText(_translate("controlWindow", "Stop"))
        self.lblEndMessage.setText(_translate("controlWindow", "Message"))
        self.txtMessageBox.setToolTip(_translate("controlWindow", "Automatic message to display when timer ends"))
        self.txtMessageBox.setStatusTip(_translate("controlWindow", "Max characters: 26"))
        self.txtMessageBox.setText(_translate("controlWindow", "Time\'s Up!"))
        self.btnSetTime.setToolTip(_translate("controlWindow", "Set countdown time duration"))
        self.btnSetTime.setText(_translate("controlWindow", "Set"))
        self.btnShowMessage.setToolTip(_translate("controlWindow", "Show message on screen now!"))
        self.btnShowMessage.setText(_translate("controlWindow", "Show"))
        self.spinSecs.setToolTip(_translate("controlWindow", "Set number of seconds"))
        self.spinSecs.setStatusTip(_translate("controlWindow", "Max Seconds: 59"))
        self.lbsCountDownTime.setText(_translate("controlWindow", "Countdown Time"))
        self.spinMins.setToolTip(_translate("controlWindow", "Set number of minutes"))
        self.spinMins.setStatusTip(_translate("controlWindow", "Max minutes: 59"))
        self.spinHrs.setToolTip(_translate("controlWindow", "Set number of hours"))
        self.spinHrs.setStatusTip(_translate("controlWindow", "Max hours: 3"))
        self.lblHours.setText(_translate("controlWindow", "Hours"))
        self.lbsMinutes.setText(_translate("controlWindow", "Minutes"))
        self.lbsSeconds.setText(_translate("controlWindow", "Seconds"))
        self.btnResetTime.setToolTip(_translate("controlWindow", "Reset countdown time duration"))
        self.btnResetTime.setText(_translate("controlWindow", "Reset"))
        self.btnHideMessage.setToolTip(_translate("controlWindow", "HIde message one screen now!"))
        self.btnHideMessage.setText(_translate("controlWindow", "Hide"))
        self.menuSettings.setTitle(_translate("controlWindow", "Settings"))
        self.menuTimer_Display.setStatusTip(_translate("controlWindow", "Launch timer display"))
        self.menuTimer_Display.setTitle(_translate("controlWindow", "Timer Display"))
        self.menuOpen_Window.setTitle(_translate("controlWindow", "Show Display"))
        self.menuHelp.setTitle(_translate("controlWindow", "Help"))
        self.actionLoad_Settings.setText(_translate("controlWindow", "Load"))
        self.actionLoad_Settings.setToolTip(_translate("controlWindow", "Load settings file"))
        self.actionLoad_Settings.setStatusTip(_translate("controlWindow", "Load settings file"))
        self.actionLoad_Settings.setShortcut(_translate("controlWindow", "Ctrl+L"))
        self.actionSave_Settings.setText(_translate("controlWindow", "Save"))
        self.actionSave_Settings.setToolTip(_translate("controlWindow", "Save current settings"))
        self.actionSave_Settings.setStatusTip(_translate("controlWindow", "Save current settings"))
        self.actionSave_Settings.setShortcut(_translate("controlWindow", "Ctrl+S"))
        self.actionExit.setText(_translate("controlWindow", "Exit"))
        self.actionExit.setToolTip(_translate("controlWindow", "Exit timer"))
        self.actionExit.setStatusTip(_translate("controlWindow", "Exit timer"))
        self.actionLaunch_in_Fullscreen.setText(_translate("controlWindow", "Fullscreen"))
        self.actionLaunch_in_Fullscreen.setStatusTip(_translate("controlWindow", "Launch timer display in fullscreen mode"))
        self.actionInteface_Help.setText(_translate("controlWindow", "Interface Help"))
        self.actionInteface_Help.setToolTip(_translate("controlWindow", "Interface Help"))
        self.actionAbout.setText(_translate("controlWindow", "About"))
        self.actionFullscreen.setText(_translate("controlWindow", "Fullscreen mode"))
        self.actionWindow_mode.setText(_translate("controlWindow", "Window mode"))
        self.actionClose_Window.setText(_translate("controlWindow", "Close Display"))
