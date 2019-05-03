# Created by: @author maapte
#
#

# Import Statements in the file

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    def close(self):
        print(self)

    def genrateExcel(self):
        print(self.lineEdit.text())

    def addStandalonePage(self):
         sampleDialog = QtWidgets.QDialog()
         sampleDialog.setWindowTitle("Automation")
         self.ui = Ui_Form()
         self.ui.setupUi(sampleDialog)
         sampleDialog.exec_()

    def addFlow(self):
         sampleDialog = QtWidgets.QDialog()
         sampleDialog.setWindowTitle("Automation")
         self.ui = Ui_Form1()
         self.ui.setupUi(sampleDialog)
         sampleDialog.exec_()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(728, 566)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 30, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 120, 111, 21))
        self.label_2.setObjectName("label_2")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(310, 120, 181, 22))
        self.lineEdit.setObjectName("lineEdit")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 170, 101, 21))
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(310, 170, 181, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 240, 91, 16))
        self.label_4.setObjectName("label_4")

        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(310, 230, 181, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(90, 290, 91, 21))
        self.label_5.setObjectName("label_5")

        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(310, 290, 181, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(60, 330, 55, 16))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(580, 140, 131, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.addStandalonePage)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(590, 210, 91, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.addFlow)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 400, 141, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.genrateExcel)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(310, 400, 121, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(QtWidgets.qApp.quit)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 728, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "   VRG Automation"))
        self.label_2.setText(_translate("MainWindow", "Project Name : "))
        self.label_3.setText(_translate("MainWindow", "Application Type :"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Ember"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Angular"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Mobile JSON"))
        self.label_4.setText(_translate("MainWindow", "Site Brand :"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "CIBC"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "CIBC USI"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "SIMPLII"))
        self.label_5.setText(_translate("MainWindow", "Site Name :"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Personal Banking"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Online Banking"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Other"))
        self.pushButton.setText(_translate("MainWindow", "Add Standalone Page"))
        self.pushButton_2.setText(_translate("MainWindow", "Add Flow"))
        self.pushButton_3.setText(_translate("MainWindow", "Generate Excel"))
        self.pushButton_4.setText(_translate("MainWindow", "Cancel"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
