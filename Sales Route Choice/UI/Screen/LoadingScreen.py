

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie


class Ui_loadingWindow(object):
    def setupUi(self, loadingWindow):
        loadingWindow.setObjectName("loadingWindow")
        loadingWindow.resize(704, 538)
        self.centralwidget = QtWidgets.QWidget(loadingWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.background = QtWidgets.QLabel(self.frame)
        self.background.setGeometry(QtCore.QRect(0, -10, loadingWindow.frameGeometry().width(), loadingWindow.frameGeometry().height()))
        self.gif = QMovie('Background/LoadingScreenBacckground.gif')
        self.background.setMovie(self.gif)
        self.gif.start()
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.Logo = QtWidgets.QLabel(self.frame)
        self.Logo.setGeometry(QtCore.QRect(550, 410, 91, 101))
        self.Logo.setPixmap(QtGui.QPixmap("Background/Avatar3.png"))
        self.Logo.setScaledContents(True)
        self.Logo.setObjectName("Logo")
        self.createdBy = QtWidgets.QLabel(self.frame)
        self.createdBy.setGeometry(QtCore.QRect(530, 375, 131, 31))
        font = QtGui.QFont()
        font.setFamily("KacstArt")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.createdBy.setFont(font)
        self.createdBy.setStyleSheet("color:rgb(121, 146, 255)")
        self.createdBy.setAlignment(QtCore.Qt.AlignCenter)
        self.createdBy.setObjectName("createdBy")
        self.appName = QtWidgets.QLabel(self.frame)
        self.appName.setGeometry(QtCore.QRect(20, 70, 681, 81))
        font = QtGui.QFont()
        font.setFamily("Waree")
        font.setPointSize(40)
        font.setItalic(True)
        self.appName.setFont(font)
        self.appName.setStyleSheet("COLOR: rgb(228, 255, 247)")
        self.appName.setAlignment(QtCore.Qt.AlignCenter)
        self.appName.setObjectName("appName")
        self.appDesc = QtWidgets.QLabel(self.frame)
        self.appDesc.setGeometry(QtCore.QRect(10, 150, 681, 41))
        font = QtGui.QFont()
        font.setFamily("Waree")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.appDesc.setFont(font)
        self.appDesc.setStyleSheet("color: White")
        self.appDesc.setAlignment(QtCore.Qt.AlignCenter)
        self.appDesc.setObjectName("appDesc")
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(30, 320, 621, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("QProgressBar\n"
"{\n"
"    background: rgb(22, 22, 22);\n"
"    color: white;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(18, 69, 89);\n"
"    color: white;\n"
"    border-radius: 2px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color:rgb(58, 113, 118);\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.appName_2 = QtWidgets.QLabel(self.frame)
        self.appName_2.setGeometry(QtCore.QRect(10, 370, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Waree")
        font.setPointSize(11)
        font.setItalic(False)
        self.appName_2.setFont(font)
        self.appName_2.setStyleSheet("COLOR: rgb(228, 255, 247)")
        self.appName_2.setAlignment(QtCore.Qt.AlignCenter)
        self.appName_2.setObjectName("appName_2")
        self.verticalLayout.addWidget(self.frame)
        loadingWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(loadingWindow)
        QtCore.QMetaObject.connectSlotsByName(loadingWindow)

    def retranslateUi(self, loadingWindow):
        _translate = QtCore.QCoreApplication.translate
        loadingWindow.setWindowTitle(_translate("loadingWindow", "MainWindow"))
        self.createdBy.setText(_translate("loadingWindow", "<strong> Created </strong> by:"))
        self.appName.setText(_translate("loadingWindow", "<strong> GENETIC </strong> ALGORITHM"))
        self.appDesc.setText(_translate("loadingWindow", "TRAVELLING SALESMAN PROBLEM"))
        self.appName_2.setText(_translate("loadingWindow", "Loading ...."))

