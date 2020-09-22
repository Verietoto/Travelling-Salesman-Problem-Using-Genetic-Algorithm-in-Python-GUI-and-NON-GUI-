"""
Hello World!!! This is a free python code of Genetic Algorithm method for word guessing problem, i made GUI Version
and nonGUI Version just it cas you guys are eager too learn about the parameters and how it affect the others.
You can use this as your reference, but dont use for commercial use.

Contact Me:

Email:      Verietoto@gmail.com
Linkedin:   www.linkedin.com/in/ketut-toto-suryahadinata-2755a9b0
"""


### Some Libraries

from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from  PyQt5.QtCore import *
import numpy as np
import time
COUNTER = 0
import sys

from UI.Screen.LoadingScreen import Ui_loadingWindow
from UI.Screen.GeneticWindow import  Ui_GeneticWindow
from UI.RouteChoosing import RouteChossing
import pandas as pd
import matplotlib
matplotlib.rcParams['figure.figsize'] = [1, 1] # for square canvas
matplotlib.rcParams['figure.subplot.left'] = 0
matplotlib.rcParams['figure.subplot.bottom'] = 0
matplotlib.rcParams['figure.subplot.right'] = 1
matplotlib.rcParams['figure.subplot.top'] = 1
matplotlib.rcParams['axes.titlesize'] = 1200
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


# Matplotlib Class
class MplCanvas(FigureCanvas):

    def __init__(self):
        """
        Class for maatplotlib
        """
        fig = Figure(figsize=(12,12), dpi=100, facecolor="Black")
        self.axes = fig.add_subplot()
        super(MplCanvas, self).__init__(fig)


#Open File Dialog Class
class openFileDialog(QWidget):
    def __init__(self):
        """
        Class for opening file dialog
        """
        super().__init__()
        self.main = QMainWindow()
        self.title = 'Opening Excels Data'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        """Setting up window geometry"""
        self.main.setWindowTitle(self.title)
        self.main.setGeometry(self.left, self.top, self.width, self.height)
        self.main.move(300,300)

        self.openFileNameDialog()

    def openFileNameDialog(self):
        """ Setting up file open in window"""
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Points Data", "",
                                                  "All Files (*.*);;Microsot Excels 2007-2013 XML(*.xlsx);;"
                                                  "Microsot Excels 2003 XML(*.xml);; Microsot Excels 97-2003 XML(*.xls)", options=options)
        if fileName != "":
            self.readPandas(fileName)

    def readPandas(self, fileName):
        """Read selected data"""
        data = pd.read_excel(fileName)
        self.names = list(data["City Names"].values)
        self.coordinate = [[x,j] for x,j in zip(data["X Coordinate"].values, data["Y Coordinate"].values)]

# Class Windiw for DashBoard
class GeneticWindow():

    def __init__(self):
        """Setting up main window"""
        self.mainWindow = QMainWindow()
        self.geneticWindow = Ui_GeneticWindow()
        self.geneticWindow.setupUi_GeneticWindow(self.mainWindow)
        self.mainWindow.move(150,200)
        self.mainWindow.setFixedSize(1012, 667)

        """Changing slider min and max"""
        self.sliderValue()

        """Connect slider to text"""
        self.geneticWindow.numberParentSlider.valueChanged.connect(lambda : self.valueChange(0))
        self.geneticWindow.mutationRateSlider.valueChanged.connect(lambda : self.valueChange(1))

        """Disabled slider initially"""
        self.disableSlider("Disabled")

        """Connect add point button to open filedialog"""
        self.geneticWindow.addPointBTN.clicked.connect(self.addData)

        """Adding lyout in screen"""
        self.screenLayout = QVBoxLayout(self.geneticWindow.screenFrame)

        """Connect Start button to start genetic algorithm"""
        self.geneticWindow.startBTN.clicked.connect(self.startGenetic)

    def startGenetic(self):
        """Start Genetic Algorithm"""

        city = self.cityNames
        coor = self.coordinate
        parentNumber = int(self.geneticWindow.NPNumber.text())
        populationNumber = int(self.geneticWindow.populationNumberInput.text())
        MR = float(self.geneticWindow.MRNumber.text())
        type = self.geneticWindow.typeSelection.currentText()
        self.genetic = RouteChossing(city=city, coor=coor,
                                     parentNum=parentNumber,
                                     popolationNum= populationNumber,
                                     mutationRate=MR,
                                     typeSelection= type)
        self.update()

    def update(self):
        """Update each Generation"""
        self.generation = 0
        indexStop = {"index": 0, "Before": None, "After": None}
        self.best = {"Route": self.genetic.city, "Distance": 1000000000, "Names": self.genetic.city}

        while self.generation < 5000:
            index = np.argmax(self.genetic.populationFitness)
            self.bestIndividu = self.genetic.population[index]
            self.bestDistance = self.genetic.populationDistance[index]
            indexStop["Before"] = self.bestDistance
            minPopulation = np.argsort(self.genetic.populationFitness)[0:len(self.genetic.children)]

            self.genetic.selectParent()
            self.genetic.createChildren()
            bestChildrenDistance = self.genetic.childrenDistance[np.argmax(self.genetic.childrenFitness)]
            bestChildrenRoute = self.genetic.children[np.argmax(self.genetic.childrenFitness)]

            if bestChildrenDistance < self.best["Distance"] - 0.3*self.best["Distance"]:
                self.best["Distance"] = bestChildrenDistance
                self.best["Route"] = [self.genetic.coordinate[x] for x in bestChildrenRoute]
                self.best["City"] = [self.genetic.city[x] for x in bestChildrenRoute]

            for i, j in enumerate(minPopulation):
                self.genetic.population[j] = self.genetic.children[i]
                self.genetic.populationFitness[j] = self.genetic.childrenFitness[i]
                self.genetic.populationDistance[j] = self.genetic.childrenDistance[i]


            indexStop["index"] += 1
            indexStop["After"] =  self.genetic.populationDistance[np.argmax(self.genetic.populationFitness)]

            self.generation +=1

            if indexStop["index"] == 150:
                break
            if indexStop["Before"] != indexStop["After"]:
                indexStop["index"] = 0
            self.updatePlot()

    def updatePlot(self):
        """Update plot every generation"""
        self.initialPlot.axes.clear()
        individu = self.bestIndividu
        coordinate = [self.genetic.coordinate[coor] for coor in individu]
        names = [self.genetic.city[coor] for coor in individu]
        xCoor = [x[0] for x in coordinate]
        yCoor = [x[1] for x in coordinate]
        self.initialPlot.axes.scatter(xCoor, yCoor, color="Red")

        for i, txt in enumerate(names):
            self.initialPlot.axes.annotate(txt, (xCoor[i], yCoor[i]),xytext=(xCoor[i]-7,yCoor[i]+7))

        self.initialPlot.axes.plot(xCoor, yCoor, color="Green")
        self.initialPlot.figure.suptitle( "Generation {} \n The Distance is: {}".format(str(self.generation), self.bestDistance))
        self.initialPlot.draw()
        self.initialPlot.flush_events()

    def addData(self):
        """Connect add data button and pick some variables"""
        mainWindow = openFileDialog()
        mainWindow.show()
        self.disableSlider("Enabled")
        self.coordinate = mainWindow.coordinate
        self.cityNames = mainWindow.names
        self.addInitialScatter()

    def addInitialScatter(self):
        """"After adding data update matplotlib scatter plot"""
        self.initialPlot = MplCanvas()
        for i in reversed(range(self.screenLayout.count())):
            self.screenLayout.itemAt(i).widget().setParent(None)
        self.screenLayout.addWidget(self.initialPlot)
        self.initialPlot.axes.clear()

        # Defines xcoor and y coor
        xCoor = [x[0] for x in self.coordinate]
        yCoor = [x[1] for x in self.coordinate]
        self.initialPlot.axes.scatter(xCoor, yCoor, color="Red")
        for i, txt in enumerate(self.cityNames):
            self.initialPlot.axes.annotate(txt, xy= (xCoor[i], yCoor[i]), xytext=(xCoor[i]-7,yCoor[i]+7))

    def disableSlider(self, type):
        """Disables some button and slider initiaally, enabled after data added"""
        featuesToDisabled = [self.geneticWindow.numberParentSlider, self.geneticWindow.mutationRateSlider, self.geneticWindow.populationNumberInput,
                             self.geneticWindow.typeSelection, self.geneticWindow.startBTN]
        if type == "Disabled":
            for i in featuesToDisabled:
                i.setDisabled(True)
        if type == "Enabled":
            for i in featuesToDisabled:
                i.setEnabled(True)

    def sliderValue(self):
        """Connect slider value to slider"""
        #Numper of Parent Slider
        self.geneticWindow.numberParentSlider.setMinimum(2)
        self.geneticWindow.numberParentSlider.setMaximum(10)
        self.geneticWindow.numberParentSlider.setTickInterval(1)

        #Mutation Rate Slider
        self.geneticWindow.mutationRateSlider.setMinimum(0)
        self.geneticWindow.mutationRateSlider.setMaximum(10)
        self.geneticWindow.mutationRateSlider.setTickInterval(1)

    def valueChange(self, index):
        """Connect number text label to slider change"""
        if index == 1:
            value = self.geneticWindow.mutationRateSlider.value()
            self.geneticWindow.MRNumber.setText(str(value/10))
        elif index ==0:
            value = self.geneticWindow.numberParentSlider.value()
            self.geneticWindow.NPNumber.setText(str(value))


class HomePage():
    def __init__(self):

        """
        Same init method in DashBoard
        """
        # Main Window
        self.mainWindow = QMainWindow()


        # Embedded Main Window to Loading Screen and move to center of screen
        self.loadingScreen = Ui_loadingWindow()
        self.loadingScreen.setupUi(self.mainWindow)
        self.mainWindow.move(300, 100)

        # Set Window into Frameless Window and show Window
        self.mainWindow.setWindowFlags(Qt.FramelessWindowHint)
        self.mainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.mainWindow.show()

        # QTimer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(40)

        # Editing Loading Text
        QtCore.QTimer.singleShot(4500,
                                 lambda: self.loadingScreen.appDesc.setText("<strong>WELCOME</strong> TO SEISTROV"))
        QtCore.QTimer.singleShot(3000,
                                 lambda: self.loadingScreen.appDesc.setText("<strong>LOADING</strong> USER INTERFACE"))
        QtCore.QTimer.singleShot(2000,
                                 lambda: self.loadingScreen.appDesc.setText("<strong>LOADING</strong> DATA BASED"))

    def progress(self):
        """
        Make a progress bar i loading window animated and close loading window after a specific time
        then open DashBoard
        :return:
        """
        global COUNTER

        self.loadingScreen.progressBar.setValue(COUNTER)
        COUNTER += 1

        if COUNTER > 100:
            self.timer.stop()
            self.mainWindow.close()
            self.geneticWindow = GeneticWindow()
            self.geneticWindow.mainWindow.show()


if __name__ == '__main__':
    app = QApplication([])
    mainWindow = HomePage()
    sys.exit(app.exec_())