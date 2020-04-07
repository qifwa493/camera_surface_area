# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QIcon('app_icon.png'))
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.redrawButton = QtWidgets.QPushButton(self.centralwidget)
        self.redrawButton.setEnabled(False)
        self.redrawButton.setObjectName("redrawButton")
        self.gridLayout.addWidget(self.redrawButton, 1, 3, 1, 1)
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setEnabled(False)
        self.cancelButton.setObjectName("cancelButton")
        self.gridLayout.addWidget(self.cancelButton, 1, 2, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 1, 0, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setResizeAnchor(QtWidgets.QGraphicsView.AnchorViewCenter)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 5)
        self.calculateButton = QtWidgets.QPushButton(self.centralwidget)
        self.calculateButton.setEnabled(False)
        self.calculateButton.setObjectName("calculateButton")
        self.gridLayout.addWidget(self.calculateButton, 1, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionHowToUse = QtWidgets.QAction(MainWindow)
        self.actionHowToUse.setObjectName("actionHowToUse")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionCreateCamMatrix = QtWidgets.QAction(MainWindow)
        self.actionCreateCamMatrix.setObjectName("actionCreateCamMatrix")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionCreateSettings")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionCreateCamMatrix)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuView.addAction(self.actionHowToUse)
        self.menuView.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Camera Surface Area"))
        self.redrawButton.setText(_translate("MainWindow", "Re-draw"))
        self.cancelButton.setText(_translate("MainWindow", "Cancel"))
        self.calculateButton.setText(_translate("MainWindow", "Calculate"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setStatusTip(_translate("MainWindow", "Import Camera Matrix and Picture"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setStatusTip(_translate("MainWindow", "Exit the program"))
        self.actionHowToUse.setText(_translate("MainWindow", "How to use"))
        self.actionHowToUse.setStatusTip(_translate("MainWindow", "How to use the program"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionAbout.setStatusTip(_translate("MainWindow", "About this program"))
        self.actionCreateCamMatrix.setText(_translate("MainWindow", "Create Camera Matrix"))
        self.actionCreateCamMatrix.setStatusTip(_translate("MainWindow", "Create a new Camera Matrix"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionSettings.setStatusTip(_translate("MainWindow", "Change settings"))

        # Custom modification
        self.actionOpen.setIcon(QIcon('Components/UI/Icons/app_open.png'))
        self.actionOpen.setShortcut('Ctrl+O')

        self.actionCreateCamMatrix.setIcon(QIcon('Components/UI/Icons/app_create.png'))
        self.actionCreateCamMatrix.setShortcut('Ctrl+N')

        self.actionSettings.setIcon(QIcon('Components/UI/Icons/app_settings.png'))
        self.actionSettings.setShortcut('Alt+S')

        self.actionExit.setIcon(QIcon('Components/UI/Icons/app_exit.png'))
        self.actionExit.setShortcut('Alt+F4')

        self.actionHowToUse.setIcon(QIcon('Components/UI/Icons/app_how.png'))
        self.actionAbout.setIcon(QIcon('Components/UI/Icons/app_about.png'))
        # End

