from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GeneticWindow(object):
    def setupUi_GeneticWindow(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1012, 667)
        MainWindow.setMinimumSize(QtCore.QSize(700, 600))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(700, 600))
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.mainFrame = QtWidgets.QFrame(self.centralwidget)
        self.mainFrame.setMinimumSize(QtCore.QSize(700, 600))
        self.mainFrame.setStyleSheet("QFrame#mainFrame{\n"
"    \n"
"    border-image: url(:/MainFrame/mainFrame.png);\n"
"\n"
"}")
        self.mainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.contentFrame = QtWidgets.QFrame(self.mainFrame)
        self.contentFrame.setGeometry(QtCore.QRect(21, 111, 59, 18))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contentFrame.sizePolicy().hasHeightForWidth())
        self.contentFrame.setSizePolicy(sizePolicy)
        self.contentFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.contentFrame.setMaximumSize(QtCore.QSize(16777215, 600))
        self.contentFrame.setStyleSheet("QFrame#contentFrame{\n"
"\n"
"border:None;\n"
"}")
        self.contentFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contentFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contentFrame.setObjectName("contentFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.contentFrame)
        self.verticalLayout_2.setContentsMargins(50, -1, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.windgedFrame = QtWidgets.QFrame(self.mainFrame)
        self.windgedFrame.setGeometry(QtCore.QRect(21, 496, 919, 120))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.windgedFrame.sizePolicy().hasHeightForWidth())
        self.windgedFrame.setSizePolicy(sizePolicy)
        self.windgedFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.windgedFrame.setMaximumSize(QtCore.QSize(16777215, 120))
        self.windgedFrame.setStyleSheet("QFrame{\n"
"\n"
"border:None;\n"
"}")
        self.windgedFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.windgedFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.windgedFrame.setObjectName("windgedFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.windgedFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.windgedFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setSizeIncrement(QtCore.QSize(2, 2))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.MRNumber = QtWidgets.QLabel(self.frame)
        self.MRNumber.setGeometry(QtCore.QRect(275, 9, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Tlwg Typist")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.MRNumber.setFont(font)
        self.MRNumber.setStyleSheet("QLabel{\n"
"    color: white;\n"
"    \n"
"\n"
"}")
        self.MRNumber.setObjectName("MRNumber")
        self.parentNumberText = QtWidgets.QLabel(self.frame)
        self.parentNumberText.setGeometry(QtCore.QRect(3, 50, 50, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.parentNumberText.sizePolicy().hasHeightForWidth())
        self.parentNumberText.setSizePolicy(sizePolicy)
        self.parentNumberText.setMaximumSize(QtCore.QSize(50, 20))
        self.parentNumberText.setStyleSheet("color:Black;")
        self.parentNumberText.setObjectName("parentNumberText")
        self.numberParentSlider = QtWidgets.QSlider(self.frame)
        self.numberParentSlider.setEnabled(True)
        self.numberParentSlider.setGeometry(QtCore.QRect(53, 45, 201, 29))
        self.numberParentSlider.setMaximumSize(QtCore.QSize(300, 16777215))
        self.numberParentSlider.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 3px solid;\n"
"    height: 4px;\n"
"    margin: 0px;\n"
"    ;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 188, 191, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    }\n"
"QSlider::handle:horizontal {\n"
"    background-color: yellow;\n"
"    border: 1px solid;\n"
"    height: 4px;\n"
"    width: 12px;\n"
"    margin: -5px 0px;\n"
"    }\n"
"QSlider::groove::disabled{\n"
"    background-color: Black;\n"
"    border: 1px solid;\n"
"    border-color: Black;\n"
"}\n"
"QSlider::handle::disabled{\n"
"    background-color: Black;\n"
"    border: 1px solid;\n"
"    border-color: Black;\n"
"}")
        self.numberParentSlider.setOrientation(QtCore.Qt.Horizontal)
        self.numberParentSlider.setObjectName("numberParentSlider")
        self.mutationRateSlider = QtWidgets.QSlider(self.frame)
        self.mutationRateSlider.setEnabled(True)
        self.mutationRateSlider.setGeometry(QtCore.QRect(56, 9, 206, 29))
        self.mutationRateSlider.setMaximumSize(QtCore.QSize(300, 16777215))
        self.mutationRateSlider.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 3px solid;\n"
"    height: 4px;\n"
"    margin: 0px;\n"
"    ;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(127, 191, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    }\n"
"QSlider::handle:horizontal {\n"
"    background-color: yellow;\n"
"    border: 1px solid;\n"
"    height: 4px;\n"
"    width: 12px;\n"
"    margin: -5px 0px;\n"
"    }\n"
"QSlider::groove::disabled{\n"
"    background-color: Black;\n"
"    border: 1px solid;\n"
"    border-color: Black;\n"
"}\n"
"QSlider::handle::disabled{\n"
"    background-color: Black;\n"
"    border: 1px solid;\n"
"    border-color: Black;\n"
"}")
        self.mutationRateSlider.setOrientation(QtCore.Qt.Horizontal)
        self.mutationRateSlider.setObjectName("mutationRateSlider")
        self.mutationRateText = QtWidgets.QLabel(self.frame)
        self.mutationRateText.setGeometry(QtCore.QRect(10, 10, 40, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mutationRateText.sizePolicy().hasHeightForWidth())
        self.mutationRateText.setSizePolicy(sizePolicy)
        self.mutationRateText.setMaximumSize(QtCore.QSize(40, 20))
        self.mutationRateText.setStyleSheet("color:Black;")
        self.mutationRateText.setObjectName("mutationRateText")
        self.NPNumber = QtWidgets.QLabel(self.frame)
        self.NPNumber.setGeometry(QtCore.QRect(274, 50, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Tlwg Typist")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.NPNumber.setFont(font)
        self.NPNumber.setStyleSheet("QLabel{\n"
"    color: white;\n"
"    \n"
"\n"
"}")
        self.NPNumber.setObjectName("NPNumber")
        self.populationNumberInput = QtWidgets.QLineEdit(self.frame)
        self.populationNumberInput.setEnabled(True)
        self.populationNumberInput.setGeometry(QtCore.QRect(310, 50, 140, 25))
        self.populationNumberInput.setMaximumSize(QtCore.QSize(140, 16777215))
        font = QtGui.QFont()
        font.setFamily("KacstDecorative")
        font.setPointSize(10)
        self.populationNumberInput.setFont(font)
        self.populationNumberInput.setStyleSheet("QLineEdit{\n"
"    background-color:white;\n"
"    color: Black;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"     select All;\n"
"}\n"
"\n"
"QLineEdit::Disabled{\n"
"    Background-color: Gray;\n"
"}")
        self.populationNumberInput.setCursorPosition(13)
        self.populationNumberInput.setAlignment(QtCore.Qt.AlignCenter)
        self.populationNumberInput.setObjectName("populationNumberInput")
        self.startBTN = QtWidgets.QPushButton(self.frame)
        self.startBTN.setEnabled(True)
        self.startBTN.setGeometry(QtCore.QRect(770, 50, 75, 27))
        self.startBTN.setMaximumSize(QtCore.QSize(140, 16777215))
        self.startBTN.setStyleSheet("QPushButton{\n"
"    background-color:Green;\n"
"    color:White;\n"
"}\n"
"\n"
"QPushButton::disabled{\n"
"    background-color: Gray;\n"
"}")
        self.startBTN.setObjectName("startBTN")
        self.addPointBTN = QtWidgets.QPushButton(self.frame)
        self.addPointBTN.setGeometry(QtCore.QRect(650, 50, 101, 27))
        self.addPointBTN.setMaximumSize(QtCore.QSize(140, 16777215))
        self.addPointBTN.setStyleSheet("background-color:Green;\n"
"color:White")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Background/add_data.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addPointBTN.setIcon(icon)
        self.addPointBTN.setObjectName("addPointBTN")
        self.typeSelection = QtWidgets.QComboBox(self.frame)
        self.typeSelection.setEnabled(True)
        self.typeSelection.setGeometry(QtCore.QRect(470, 50, 151, 27))
        self.typeSelection.setStyleSheet("QComboBox::Disabled{\n"
"    background-color: Gray;\n"
"}")
        self.typeSelection.setObjectName("typeSelection")
        self.typeSelection.addItem("")
        self.typeSelection.addItem("")
        self.typeSelection.addItem("")
        self.selectionTypeText = QtWidgets.QLabel(self.frame)
        self.selectionTypeText.setGeometry(QtCore.QRect(470, 30, 121, 17))
        self.selectionTypeText.setStyleSheet("color:White;\n"
"background-color:None")
        self.selectionTypeText.setObjectName("selectionTypeText")
        self.horizontalLayout.addWidget(self.frame)
        self.screenFrame = QtWidgets.QFrame(self.mainFrame)
        self.screenFrame.setGeometry(QtCore.QRect(20, 20, 961, 441))
        self.screenFrame.setStyleSheet("background-color: rgba(255, 255, 255);")
        self.screenFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.screenFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.screenFrame.setObjectName("screenFrame")
        self.horizontalLayout_2.addWidget(self.mainFrame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.MRNumber.setText(_translate("MainWindow", "0"))
        self.parentNumberText.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">NP</span></p><p align=\"center\"><span style=\" color:#ffffff;\"><br/></span></p></body></html>"))
        self.mutationRateText.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">MR</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\"><br/></span></p></body></html>"))
        self.NPNumber.setText(_translate("MainWindow", "2"))
        self.populationNumberInput.setText(_translate("MainWindow", "Population No"))
        self.startBTN.setText(_translate("MainWindow", "Start"))
        self.addPointBTN.setText(_translate("MainWindow", "Add Point"))
        self.typeSelection.setItemText(0, _translate("MainWindow", "Ranks"))
        self.typeSelection.setItemText(1, _translate("MainWindow", "Roulette"))
        self.typeSelection.setItemText(2, _translate("MainWindow", "Random"))
        self.selectionTypeText.setText(_translate("MainWindow", "Selection Type"))
import UI.Background.MainFrame_rc
