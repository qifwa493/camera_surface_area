# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_settingsDialog(object):
    def setupUi(self, settingsDialog):
        settingsDialog.setObjectName("settingsDialog")
        settingsDialog.resize(400, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(settingsDialog.sizePolicy().hasHeightForWidth())
        settingsDialog.setSizePolicy(sizePolicy)
        settingsDialog.setMinimumSize(QtCore.QSize(400, 300))
        settingsDialog.setMaximumSize(QtCore.QSize(400, 300))
        self.gridLayout_5 = QtWidgets.QGridLayout(settingsDialog)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.modeSelectionGroup = QtWidgets.QGroupBox(settingsDialog)
        self.modeSelectionGroup.setObjectName("modeSelectionGroup")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.modeSelectionGroup)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.atuoModeButton = QtWidgets.QRadioButton(self.modeSelectionGroup)
        self.atuoModeButton.setCheckable(True)
        self.atuoModeButton.setChecked(True)
        self.atuoModeButton.setAutoRepeat(True)
        self.atuoModeButton.setObjectName("atuoModeButton")
        self.gridLayout.addWidget(self.atuoModeButton, 0, 1, 1, 1)
        self.manualModeButton = QtWidgets.QRadioButton(self.modeSelectionGroup)
        self.manualModeButton.setObjectName("manualModeButton")
        self.gridLayout.addWidget(self.manualModeButton, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.modeSelectionGroup, 0, 0, 1, 1)
        self.unitSizeGroup = QtWidgets.QGroupBox(settingsDialog)
        self.unitSizeGroup.setObjectName("unitSizeGroup")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.unitSizeGroup)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.unitSizeSlider = QtWidgets.QSlider(self.unitSizeGroup)
        self.unitSizeSlider.setMinimum(200)
        self.unitSizeSlider.setMaximum(300)
        self.unitSizeSlider.setSliderPosition(250)
        self.unitSizeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.unitSizeSlider.setObjectName("unitSizeSlider")
        self.gridLayout_4.addWidget(self.unitSizeSlider, 0, 0, 1, 1)
        self.unitSizeSpinBox = QtWidgets.QSpinBox(self.unitSizeGroup)
        self.unitSizeSpinBox.setMinimum(200)
        self.unitSizeSpinBox.setMaximum(300)
        self.unitSizeSpinBox.setProperty("value", 250)
        self.unitSizeSpinBox.setObjectName("unitSizeSpinBox")
        self.gridLayout_4.addWidget(self.unitSizeSpinBox, 0, 1, 1, 1)
        self.gridLayout_5.addWidget(self.unitSizeGroup, 1, 0, 1, 1)
        self.curveFittingBox = QtWidgets.QCheckBox(settingsDialog)
        self.curveFittingBox.setObjectName("curveFittingBox")
        self.gridLayout_5.addWidget(self.curveFittingBox, 2, 0, 1, 1)
        self.maxSizeGroup = QtWidgets.QGroupBox(settingsDialog)
        self.maxSizeGroup.setObjectName("maxSizeGroup")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.maxSizeGroup)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.maxSizeSlider = QtWidgets.QSlider(self.maxSizeGroup)
        self.maxSizeSlider.setMinimum(1000)
        self.maxSizeSlider.setMaximum(5000)
        self.maxSizeSlider.setProperty("value", 3000)
        self.maxSizeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.maxSizeSlider.setObjectName("maxSizeSlider")
        self.gridLayout_3.addWidget(self.maxSizeSlider, 0, 0, 1, 1)
        self.maxSizeSpinBox = QtWidgets.QSpinBox(self.maxSizeGroup)
        self.maxSizeSpinBox.setMinimum(1000)
        self.maxSizeSpinBox.setMaximum(5000)
        self.maxSizeSpinBox.setProperty("value", 3000)
        self.maxSizeSpinBox.setObjectName("maxSizeSpinBox")
        self.gridLayout_3.addWidget(self.maxSizeSpinBox, 0, 1, 1, 1)
        self.gridLayout_5.addWidget(self.maxSizeGroup, 3, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(settingsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_5.addWidget(self.buttonBox, 4, 0, 1, 1)

        self.retranslateUi(settingsDialog)
        self.buttonBox.accepted.connect(settingsDialog.accept)
        self.buttonBox.rejected.connect(settingsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(settingsDialog)

    def retranslateUi(self, settingsDialog):
        _translate = QtCore.QCoreApplication.translate
        settingsDialog.setWindowTitle(_translate("settingsDialog", "Settings"))
        self.modeSelectionGroup.setTitle(_translate("settingsDialog", "Area selection mode"))
        self.atuoModeButton.setText(_translate("settingsDialog", "Auto"))
        self.manualModeButton.setText(_translate("settingsDialog", "Manual"))
        self.unitSizeGroup.setTitle(_translate("settingsDialog", "Chessboard Unit size (*10^-4 m)"))
        self.curveFittingBox.setText(_translate("settingsDialog", "Curve fitting"))
        self.maxSizeGroup.setTitle(_translate("settingsDialog", "Max image size during processing"))
