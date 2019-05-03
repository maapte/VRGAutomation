# Import Statements in the file





from PyQt5 import QtCore, QtGui, QtWidgets
from steps import Ui_StepWindow
from FormsPage import FormsPage
import json


class Ui_Form15(object):

    def setupUi(self, Form):

        Form.setObjectName("Form")
        Form.resize(572, 352)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(40, 30, 501, 201))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(50, 30, 91, 21))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(150, 30, 161, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(50, 80, 91, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 80, 161, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(40, 140, 81, 20))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setGeometry(QtCore.QRect(140, 140, 121, 21))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_3.setGeometry(QtCore.QRect(270, 140, 81, 20))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_4.setGeometry(QtCore.QRect(340, 140, 81, 20))
        self.checkBox_4.setObjectName("checkBox_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(120, 260, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 260, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        obj = FormsPage()
        obj.set_formName(self.lineEdit.text())
        obj.set_noOfSteps(self.lineEdit_2.text())
        obj.set_isProductExist(self.checkBox.isVisible())
        obj.set_isTransactionExist(self.checkBox_2.isVisible())
        x = json.dumps(obj.__dict__)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Form Information"))
        self.label.setText(_translate("Form", "Form Name:"))
        self.label_2.setText(_translate("Form", "No. of Step"))
        self.checkBox.setText(_translate("Form", "Products"))
        self.checkBox_2.setText(_translate("Form", " Transaction"))
        self.checkBox_3.setText(_translate("Form", "DSR"))
        self.checkBox_4.setText(_translate("Form", "Other"))
        self.pushButton.setText(_translate("Form", "OK"))
        self.pushButton_2.setText(_translate("Form", "Cancel"))


    def addStep(self, param):
        print("!!!!!!!!!!!!!")
        print(param)
        sampleDialog = QtWidgets.QDialog()
        sampleDialog.setWindowTitle("Automation")
        self.ui = Ui_StepWindow()
        self.ui.setupUi(sampleDialog, param)
        sampleDialog.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form15()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
