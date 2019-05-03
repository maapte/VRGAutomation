# author @maapte

import json

from PyQt5 import QtCore, QtGui, QtWidgets

from FormsPage import FormsPage
# import models
from StandalonePage import StandalonePage
from StepsPage import StepsPage
from app import AppVRG
from vrg import Vrg


class Ui_c(object):

    # obj is an object of the class Vrg
    def __init__(self):
        self.vrg = Vrg()
        self.formObj = FormsPage()

    def setupUi(self, c):
        c.setObjectName("c")
        c.resize(1905, 985)
        c.setWindowIcon(QtGui.QIcon('cibc.png'))
        self.centralwidget = QtWidgets.QWidget(c)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(380, 20, 211, 21))

        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.projectName_label = QtWidgets.QLabel(self.centralwidget)
        self.projectName_label.setGeometry(QtCore.QRect(20, 70, 101, 31))
        self.projectName_label.setObjectName("projectName_label")

        self.projectName = QtWidgets.QLineEdit(self.centralwidget)
        self.projectName.setGeometry(QtCore.QRect(150, 70, 231, 31))
        self.projectName.setObjectName("projectName")

        self.userName_label = QtWidgets.QLabel(self.centralwidget)
        self.userName_label.setGeometry(QtCore.QRect(490, 60, 71, 31))
        self.userName_label.setObjectName("userName_label")

        self.userName = QtWidgets.QLineEdit(self.centralwidget)
        self.userName.setGeometry(QtCore.QRect(620, 70, 241, 31))
        self.userName.setObjectName("userName")

        self.brand_label = QtWidgets.QLabel(self.centralwidget)
        self.brand_label.setGeometry(QtCore.QRect(20, 130, 55, 16))
        self.brand_label.setObjectName("brand_label")

        self.brand_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.brand_combobox.setGeometry(QtCore.QRect(150, 130, 231, 22))
        self.brand_combobox.setObjectName("brand_combobox")
        self.brand_combobox.addItem("")
        self.brand_combobox.setItemText(0, "")
        self.brand_combobox.addItem("")
        self.brand_combobox.addItem("")
        self.brand_combobox.addItem("")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(490, 130, 111, 16))
        self.label_6.setObjectName("label_6")

        self.appliType_combo = QtWidgets.QComboBox(self.centralwidget)
        self.appliType_combo.setGeometry(QtCore.QRect(620, 130, 231, 22))
        self.appliType_combo.setObjectName("appliType_combo")
        self.appliType_combo.addItem("")
        self.appliType_combo.setItemText(0, "")
        self.appliType_combo.addItem("")
        self.appliType_combo.addItem("")
        self.appliType_combo.addItem("")
        self.appliType_combo.currentIndexChanged.connect(self.applicationType)

        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(180, 240, 93, 28))
        self.addButton.setObjectName("addButton")
        self.addButton.clicked.connect(self.add_page_button)

        self.addFlow = QtWidgets.QPushButton(self.centralwidget)
        self.addFlow.setGeometry(QtCore.QRect(500, 240, 93, 28))
        self.addFlow.setObjectName("addFlow")
        self.addFlow.clicked.connect(self.addFlow_Page)

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(60, 370, 55, 16))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")

        self.standAlonePageBox = QtWidgets.QGroupBox(self.centralwidget)
        self.standAlonePageBox.setGeometry(QtCore.QRect(30, 290, 421, 351))
        self.standAlonePageBox.setObjectName("standAlonePageBox")

        self.pageName = QtWidgets.QLabel(self.standAlonePageBox)
        self.pageName.setGeometry(QtCore.QRect(50, 40, 91, 21))
        self.pageName.setObjectName("pageName")

        self.pageName_2 = QtWidgets.QLineEdit(self.standAlonePageBox)
        self.pageName_2.setGeometry(QtCore.QRect(150, 40, 191, 31))
        self.pageName_2.setObjectName("pageName_2")

        self.errorGroupBoxPage = QtWidgets.QGroupBox(self.standAlonePageBox)
        self.errorGroupBoxPage.setGeometry(QtCore.QRect(50, 99, 291, 61))
        self.errorGroupBoxPage.setObjectName("errorGroupBoxPage")

        self.yes = QtWidgets.QRadioButton(self.errorGroupBoxPage)
        self.yes.setGeometry(QtCore.QRect(70, 20, 95, 20))
        self.yes.setObjectName("yes")

        self.no = QtWidgets.QRadioButton(self.errorGroupBoxPage)
        self.no.setGeometry(QtCore.QRect(140, 20, 95, 20))
        self.no.setObjectName("no")

        self.loginGroupBoxPage = QtWidgets.QGroupBox(self.standAlonePageBox)
        self.loginGroupBoxPage.setGeometry(QtCore.QRect(50, 170, 291, 80))
        self.loginGroupBoxPage.setObjectName("loginGroupBoxPage")

        self.yes_2 = QtWidgets.QRadioButton(self.loginGroupBoxPage)
        self.yes_2.setGeometry(QtCore.QRect(20, 30, 95, 20))
        self.yes_2.setObjectName("yes_2")

        self.no_2 = QtWidgets.QRadioButton(self.loginGroupBoxPage)
        self.no_2.setGeometry(QtCore.QRect(80, 30, 95, 20))
        self.no_2.setObjectName("no_2")

        self.both = QtWidgets.QRadioButton(self.loginGroupBoxPage)
        self.both.setGeometry(QtCore.QRect(150, 30, 95, 20))
        self.both.setObjectName("both")

        self.saveButton = QtWidgets.QPushButton(self.standAlonePageBox)
        self.saveButton.setGeometry(QtCore.QRect(50, 270, 93, 28))
        self.saveButton.setObjectName("saveButton")
        self.saveButton.clicked.connect(self.saveStandalonePage)

        self.cancelButton = QtWidgets.QPushButton(self.standAlonePageBox)
        self.cancelButton.setGeometry(QtCore.QRect(200, 270, 93, 28))
        self.cancelButton.setObjectName("cancelButton")

        self.standAlonePageBox.setEnabled(False)

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(150, 180, 231, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.currentIndexChanged.connect(self.siteType)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 180, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(490, 180, 81, 16))
        self.label_3.setObjectName("label_3")
        self.siteName = QtWidgets.QLineEdit(self.centralwidget)
        self.siteName.setGeometry(QtCore.QRect(620, 170, 231, 31))
        self.siteName.setObjectName("siteName")
        self.formGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.formGroupBox.setGeometry(QtCore.QRect(460, 290, 411, 351))
        self.formGroupBox.setObjectName("formGroupBox")
        self.label_4 = QtWidgets.QLabel(self.formGroupBox)
        self.label_4.setGeometry(QtCore.QRect(30, 50, 91, 31))
        self.label_4.setObjectName("label_4")
        self.formName = QtWidgets.QLineEdit(self.formGroupBox)
        self.formName.setGeometry(QtCore.QRect(150, 50, 201, 31))
        self.formName.setObjectName("formName")
        self.label_5 = QtWidgets.QLabel(self.formGroupBox)
        self.label_5.setGeometry(QtCore.QRect(40, 130, 91, 16))
        self.label_5.setObjectName("label_5")
        self.noOfSteps = QtWidgets.QLineEdit(self.formGroupBox)
        self.noOfSteps.setGeometry(QtCore.QRect(150, 120, 201, 31))
        self.noOfSteps.setObjectName("noOfSteps")
        self.productCheckbox = QtWidgets.QCheckBox(self.formGroupBox)
        self.productCheckbox.setGeometry(QtCore.QRect(50, 200, 81, 20))
        self.productCheckbox.setObjectName("productCheckbox")
        self.transactionCheckbox = QtWidgets.QCheckBox(self.formGroupBox)
        self.transactionCheckbox.setGeometry(QtCore.QRect(160, 200, 111, 20))
        self.transactionCheckbox.setObjectName("transactionCheckbox")
        self.dsr = QtWidgets.QCheckBox(self.formGroupBox)
        self.dsr.setGeometry(QtCore.QRect(290, 200, 81, 20))
        self.dsr.setObjectName("dsr")
        self.generateSteps = QtWidgets.QPushButton(self.formGroupBox)
        self.generateSteps.setGeometry(QtCore.QRect(120, 260, 121, 28))
        self.generateSteps.setObjectName("generateSteps")
        self.generateSteps.clicked.connect(self.save_form_page)
        self.formGroupBox.setEnabled(False)

        self.stepGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.stepGroupBox.setGeometry(QtCore.QRect(890, 20, 1001, 791))
        self.stepGroupBox.setObjectName("stepGroupBox")

        self.pageNameLabelSteps = QtWidgets.QLabel(self.stepGroupBox)
        self.pageNameLabelSteps.setGeometry(QtCore.QRect(50, 40, 91, 16))
        self.pageNameLabelSteps.setObjectName("pageNameLabelSteps")
        self.pageNameStepsTextbox = QtWidgets.QLineEdit(self.stepGroupBox)
        self.pageNameStepsTextbox.setGeometry(QtCore.QRect(140, 30, 181, 31))
        self.pageNameStepsTextbox.setObjectName("pageNameStepsTextbox")

        self.stepNameLabel = QtWidgets.QLabel(self.stepGroupBox)
        self.stepNameLabel.setGeometry(QtCore.QRect(520, 40, 81, 16))
        self.stepNameLabel.setObjectName("stepNameLabel")
        self.stepNameTextbox = QtWidgets.QLineEdit(self.stepGroupBox)
        self.stepNameTextbox.setGeometry(QtCore.QRect(610, 30, 201, 31))
        self.stepNameTextbox.setObjectName("stepNameTextbox")

        self.loginGroupboxSteps = QtWidgets.QGroupBox(self.stepGroupBox)
        self.loginGroupboxSteps.setGeometry(QtCore.QRect(50, 90, 351, 91))
        self.loginGroupboxSteps.setObjectName("loginGroupboxSteps")

        self.yesLoginSteps = QtWidgets.QRadioButton(self.loginGroupboxSteps)
        self.yesLoginSteps.setGeometry(QtCore.QRect(10, 40, 95, 20))
        self.yesLoginSteps.setObjectName("yesLoginSteps")

        self.nologinSteps = QtWidgets.QRadioButton(self.loginGroupboxSteps)
        self.nologinSteps.setGeometry(QtCore.QRect(110, 40, 95, 20))
        self.nologinSteps.setObjectName("nologinSteps")

        self.bothLoginSteps = QtWidgets.QRadioButton(self.loginGroupboxSteps)
        self.bothLoginSteps.setGeometry(QtCore.QRect(220, 40, 95, 20))
        self.bothLoginSteps.setObjectName("bothLoginSteps")

        self.formGroupBoxSteps = QtWidgets.QGroupBox(self.stepGroupBox)
        self.formGroupBoxSteps.setGeometry(QtCore.QRect(470, 230, 531, 91))
        self.formGroupBoxSteps.setObjectName("formGroupBoxSteps")

        self.formView = QtWidgets.QCheckBox(self.formGroupBoxSteps)
        self.formView.setGeometry(QtCore.QRect(130, 20, 121, 20))
        self.formView.setObjectName("formView")

        self.formSubmit = QtWidgets.QCheckBox(self.formGroupBoxSteps)
        self.formSubmit.setGeometry(QtCore.QRect(130, 60, 121, 20))
        self.formSubmit.setObjectName("formSubmit")

        self.formQualify = QtWidgets.QCheckBox(self.formGroupBoxSteps)
        self.formQualify.setGeometry(QtCore.QRect(390, 20, 161, 20))
        self.formQualify.setObjectName("formQualify")

        self.formSteps = QtWidgets.QCheckBox(self.formGroupBoxSteps)
        self.formSteps.setGeometry(QtCore.QRect(390, 60, 101, 20))
        self.formSteps.setObjectName("formSteps")

        self.groupBox_5 = QtWidgets.QGroupBox(self.formGroupBoxSteps)
        self.groupBox_5.setGeometry(QtCore.QRect(630, 90, 301, 80))
        self.groupBox_5.setObjectName("groupBox_5")

        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_4.setGeometry(QtCore.QRect(40, 30, 95, 20))
        self.radioButton_4.setObjectName("radioButton_4")

        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_5.setGeometry(QtCore.QRect(120, 30, 95, 20))
        self.radioButton_5.setObjectName("radioButton_5")

        self.productGroupBoxSteps = QtWidgets.QGroupBox(self.stepGroupBox)
        self.productGroupBoxSteps.setGeometry(QtCore.QRect(40, 400, 971, 301))
        self.productGroupBoxSteps.setObjectName("productGroupBoxSteps")
        self.productAppGroupboxSteps = QtWidgets.QGroupBox(self.productGroupBoxSteps)
        self.productAppGroupboxSteps.setGeometry(QtCore.QRect(30, 140, 891, 131))
        self.productAppGroupboxSteps.setObjectName("productAppGroupboxSteps")
        self.personalDetails = QtWidgets.QCheckBox(self.productAppGroupboxSteps)
        self.personalDetails.setGeometry(QtCore.QRect(120, 30, 161, 20))
        self.personalDetails.setObjectName("personalDetails")
        self.summary = QtWidgets.QCheckBox(self.productAppGroupboxSteps)
        self.summary.setGeometry(QtCore.QRect(340, 30, 81, 21))
        self.summary.setObjectName("summary")
        self.confirmation = QtWidgets.QCheckBox(self.productAppGroupboxSteps)
        self.confirmation.setGeometry(QtCore.QRect(550, 30, 131, 20))
        self.confirmation.setObjectName("confirmation")
        self.productRecommendation = QtWidgets.QCheckBox(self.productAppGroupboxSteps)
        self.productRecommendation.setGeometry(QtCore.QRect(120, 60, 171, 20))
        self.productRecommendation.setObjectName("productRecommendation")
        self.termsandcondition = QtWidgets.QCheckBox(self.productAppGroupboxSteps)
        self.termsandcondition.setGeometry(QtCore.QRect(340, 60, 181, 20))
        self.termsandcondition.setObjectName("termsandcondition")
        self.isPaperless = QtWidgets.QCheckBox(self.productAppGroupboxSteps)
        self.isPaperless.setGeometry(QtCore.QRect(550, 60, 111, 20))
        self.isPaperless.setObjectName("isPaperless")
        self.productIdLabel = QtWidgets.QLabel(self.productGroupBoxSteps)
        self.productIdLabel.setGeometry(QtCore.QRect(10, 40, 91, 16))
        self.productIdLabel.setObjectName("productIdLabel")
        self.productId = QtWidgets.QLineEdit(self.productGroupBoxSteps)
        self.productId.setGeometry(QtCore.QRect(120, 30, 161, 31))
        self.productId.setObjectName("productId")
        self.parentProductLabel = QtWidgets.QLabel(self.productGroupBoxSteps)
        self.parentProductLabel.setGeometry(QtCore.QRect(320, 40, 121, 16))
        self.parentProductLabel.setObjectName("parentProductLabel")
        self.parentProduct = QtWidgets.QLineEdit(self.productGroupBoxSteps)
        self.parentProduct.setGeometry(QtCore.QRect(430, 30, 181, 31))
        self.parentProduct.setObjectName("parentProduct")
        self.adJudicationLabel = QtWidgets.QLabel(self.productGroupBoxSteps)
        self.adJudicationLabel.setGeometry(QtCore.QRect(630, 40, 121, 16))
        self.adJudicationLabel.setObjectName("adJudicationLabel")
        self.adjudication = QtWidgets.QLineEdit(self.productGroupBoxSteps)
        self.adjudication.setGeometry(QtCore.QRect(720, 30, 181, 31))
        self.adjudication.setObjectName("adjudication")
        self.positioningLabel = QtWidgets.QLabel(self.productGroupBoxSteps)
        self.positioningLabel.setGeometry(QtCore.QRect(10, 90, 111, 16))
        self.positioningLabel.setObjectName("positioningLabel")
        self.positioning_combobox = QtWidgets.QComboBox(self.productGroupBoxSteps)
        self.positioning_combobox.setGeometry(QtCore.QRect(120, 90, 161, 22))
        self.positioning_combobox.setObjectName("positioning_combobox")
        self.positioning_combobox.addItem("")
        self.positioning_combobox.addItem("")
        self.positioning_combobox.addItem("")
        self.positioning_combobox.addItem("")
        self.positioning_combobox.addItem("")
        self.positioning_combobox.addItem("")
        self.groupingLabel = QtWidgets.QLabel(self.productGroupBoxSteps)
        self.groupingLabel.setGeometry(QtCore.QRect(330, 90, 55, 16))
        self.groupingLabel.setObjectName("groupingLabel")
        self.grouping_combobox = QtWidgets.QComboBox(self.productGroupBoxSteps)
        self.grouping_combobox.setGeometry(QtCore.QRect(430, 90, 181, 22))
        self.grouping_combobox.setObjectName("grouping_combobox")
        self.grouping_combobox.addItem("")
        self.grouping_combobox.addItem("")
        self.grouping_combobox.addItem("")
        self.grouping_combobox.addItem("")
        self.fulfillmentLabel = QtWidgets.QLabel(self.productGroupBoxSteps)
        self.fulfillmentLabel.setGeometry(QtCore.QRect(640, 90, 71, 16))
        self.fulfillmentLabel.setObjectName("fulfillmentLabel")
        self.fulfillment_comboBox = QtWidgets.QComboBox(self.productGroupBoxSteps)
        self.fulfillment_comboBox.setGeometry(QtCore.QRect(720, 90, 181, 22))
        self.fulfillment_comboBox.setObjectName("fulfillment_comboBox")
        self.fulfillment_comboBox.addItem("")
        self.fulfillment_comboBox.addItem("")
        self.fulfillment_comboBox.addItem("")
        self.fulfillment_comboBox.addItem("")
        self.fulfillment_comboBox.addItem("")
        self.fulfillment_comboBox.addItem("")
        self.transactionGroupBoxSteps = QtWidgets.QGroupBox(self.stepGroupBox)
        self.transactionGroupBoxSteps.setGeometry(QtCore.QRect(50, 190, 351, 191))
        self.transactionGroupBoxSteps.setObjectName("transactionGroupBoxSteps")
        self.formStepsLabel = QtWidgets.QLabel(self.transactionGroupBoxSteps)
        self.formStepsLabel.setGeometry(QtCore.QRect(40, 40, 55, 16))
        self.formStepsLabel.setObjectName("formStepsLabel")
        self.formStepTextBox = QtWidgets.QLineEdit(self.transactionGroupBoxSteps)
        self.formStepTextBox.setGeometry(QtCore.QRect(130, 40, 151, 31))
        self.formStepTextBox.setObjectName("formStepTextBox")
        self.toStepsLabel = QtWidgets.QLabel(self.transactionGroupBoxSteps)
        self.toStepsLabel.setGeometry(QtCore.QRect(30, 90, 55, 16))
        self.toStepsLabel.setObjectName("toStepsLabel")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.transactionGroupBoxSteps)
        self.lineEdit_13.setGeometry(QtCore.QRect(130, 90, 151, 31))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.isExternalCheckbox = QtWidgets.QCheckBox(self.transactionGroupBoxSteps)
        self.isExternalCheckbox.setGeometry(QtCore.QRect(130, 140, 141, 20))
        self.isExternalCheckbox.setObjectName("isExternalCheckbox")
        self.errorGroupboxSteps = QtWidgets.QGroupBox(self.stepGroupBox)
        self.errorGroupboxSteps.setGeometry(QtCore.QRect(510, 80, 411, 101))
        self.errorGroupboxSteps.setObjectName("errorGroupboxSteps")
        self.yesErrorSteps = QtWidgets.QRadioButton(self.errorGroupboxSteps)
        self.yesErrorSteps.setGeometry(QtCore.QRect(50, 50, 95, 20))
        self.yesErrorSteps.setObjectName("yesErrorSteps")
        self.noErrorSteps = QtWidgets.QRadioButton(self.errorGroupboxSteps)
        self.noErrorSteps.setGeometry(QtCore.QRect(170, 50, 95, 20))
        self.noErrorSteps.setObjectName("noErrorSteps")

        self.saveandNext = QtWidgets.QPushButton(self.stepGroupBox)
        self.saveandNext.setGeometry(QtCore.QRect(380, 720, 93, 28))
        self.saveandNext.setObjectName("saveandNext")
        self.saveandNext.clicked.connect(self.save_steps_information)

        self.cancelSteps = QtWidgets.QPushButton(self.stepGroupBox)
        self.cancelSteps.setGeometry(QtCore.QRect(510, 720, 93, 28))
        self.cancelSteps.setObjectName("cancelSteps")
        self.stepGroupBox.setEnabled(False)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(740, 830, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.generatevrgdocument)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(870, 830, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.close)

        c.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(c)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1905, 26))
        self.menubar.setObjectName("menubar")
        c.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(c)
        self.statusbar.setObjectName("statusbar")
        c.setStatusBar(self.statusbar)

        self.retranslateUi(c)
        QtCore.QMetaObject.connectSlotsByName(c)

    def retranslateUi(self, c):
        _translate = QtCore.QCoreApplication.translate
        # c.setWindowTitle(_translate("c", "MainWindow"))
        c.setWindowTitle(_translate("c", "CIBC VRG Automation"))
        self.label.setText(_translate("c", "       VRG Automation"))
        self.projectName_label.setText(_translate("c", "Project Name :"))
        self.userName_label.setText(_translate("c", "Prepared By: "))
        self.brand_label.setText(_translate("c", "Brand :"))
        self.brand_combobox.setItemText(1, _translate("c", "CIBC"))
        self.brand_combobox.setItemText(2, _translate("c", "CIBC US"))
        self.brand_combobox.setItemText(3, _translate("c", "SIMPLII"))
        self.label_6.setText(_translate("c", "Application Type :"))
        self.appliType_combo.setItemText(1, _translate("c", "Ember"))
        self.appliType_combo.setItemText(2, _translate("c", "Angular"))
        self.appliType_combo.setItemText(3, _translate("c", "Mobile JSON"))
        self.addButton.setText(_translate("c", "Add Page"))
        self.addFlow.setText(_translate("c", "Add Flow"))
        self.standAlonePageBox.setTitle(_translate("c", "StandAlone Page"))
        self.pageName.setText(_translate("c", "Page Name :"))
        self.errorGroupBoxPage.setTitle(_translate("c", "Error"))
        self.yes.setText(_translate("c", "Yes"))
        self.no.setText(_translate("c", "No"))
        self.loginGroupBoxPage.setTitle(_translate("c", "Login"))
        self.yes_2.setText(_translate("c", "Yes"))
        self.no_2.setText(_translate("c", "No"))
        self.both.setText(_translate("c", "Both"))
        self.saveButton.setText(_translate("c", "Save"))
        self.cancelButton.setText(_translate("c", "Cancel"))
        self.comboBox.setItemText(1, _translate("c", "Desktop"))
        self.comboBox.setItemText(2, _translate("c", "Mobile"))
        self.comboBox.setItemText(3, _translate("c", "Responsive"))
        self.label_2.setText(_translate("c", "Site Type : "))
        self.label_3.setText(_translate("c", "Site Name :"))
        self.formGroupBox.setTitle(_translate("c", "Fom Flow"))
        self.label_4.setText(_translate("c", "Form Name :"))
        self.label_5.setText(_translate("c", "No. Of Steps : "))
        self.productCheckbox.setText(_translate("c", "Products"))
        self.transactionCheckbox.setText(_translate("c", "Transaction"))
        self.dsr.setText(_translate("c", "DSR"))
        self.generateSteps.setText(_translate("c", "Generate Steps"))
        self.stepGroupBox.setTitle(_translate("c", "Steps"))
        self.pageNameLabelSteps.setText(_translate("c", "Page Name"))
        self.stepNameLabel.setText(_translate("c", "Step Name :"))
        self.loginGroupboxSteps.setTitle(_translate("c", "Login"))
        self.yesLoginSteps.setText(_translate("c", "Yes"))
        self.nologinSteps.setText(_translate("c", "No"))
        self.bothLoginSteps.setText(_translate("c", "Both"))
        self.formGroupBoxSteps.setTitle(_translate("c", " Form Steps"))
        self.formView.setText(_translate("c", " Form View"))
        self.formSubmit.setText(_translate("c", "Form Submit"))
        self.formQualify.setText(_translate("c", "Form Qualify"))
        self.formSteps.setText(_translate("c", "Form Steps"))
        self.groupBox_5.setTitle(_translate("c", "Error"))
        self.radioButton_4.setText(_translate("c", "Yes"))
        self.radioButton_5.setText(_translate("c", "No"))
        self.productGroupBoxSteps.setTitle(_translate("c", "Product Information"))
        self.productAppGroupboxSteps.setTitle(_translate("c", "Product Application Steps"))
        self.personalDetails.setText(_translate("c", "Personal Details"))
        self.summary.setText(_translate("c", "Summary"))
        self.confirmation.setText(_translate("c", "Confirmation"))
        self.productRecommendation.setText(_translate("c", "Product Recommendation"))
        self.termsandcondition.setText(_translate("c", "Terms and Condition"))
        self.isPaperless.setText(_translate("c", "Is Paperless"))
        self.productIdLabel.setText(_translate("c", "Product Id :"))
        self.parentProductLabel.setText(_translate("c", "Parent Product"))
        self.adJudicationLabel.setText(_translate("c", "Adjudication"))
        self.positioningLabel.setText(_translate("c", "Postioning:"))
        self.positioning_combobox.setItemText(0, _translate("c", "Not Applicable"))
        self.positioning_combobox.setItemText(1, _translate("c", "Upsell"))
        self.positioning_combobox.setItemText(2, _translate("c", "downsell"))
        self.positioning_combobox.setItemText(3, _translate("c", "user selected"))
        self.positioning_combobox.setItemText(4, _translate("c", "system recommended"))
        self.positioning_combobox.setItemText(5, _translate("c", "Dynamic"))
        self.groupingLabel.setText(_translate("c", "Grouping"))
        self.grouping_combobox.setItemText(0, _translate("c", "Not Applicable"))
        self.grouping_combobox.setItemText(1, _translate("c", "Bundle Id"))
        self.grouping_combobox.setItemText(2, _translate("c", "No Grouping"))
        self.grouping_combobox.setItemText(3, _translate("c", "Dynamic"))
        self.fulfillmentLabel.setText(_translate("c", "Fulfillment :"))
        self.fulfillment_comboBox.setItemText(0, _translate("c", "Not Applicable"))
        self.fulfillment_comboBox.setItemText(1, _translate("c", "Branch"))
        self.fulfillment_comboBox.setItemText(2, _translate("c", "ESIG"))
        self.fulfillment_comboBox.setItemText(3, _translate("c", "RDC"))
        self.fulfillment_comboBox.setItemText(4, _translate("c", "Direct"))
        self.fulfillment_comboBox.setItemText(5, _translate("c", "Dynamic"))

        self.transactionGroupBoxSteps.setTitle(_translate("c", "Transaction"))
        self.formStepsLabel.setText(_translate("c", "From : "))
        self.toStepsLabel.setText(_translate("c", "  To:"))
        self.isExternalCheckbox.setText(_translate("c", "Is External"))

        self.errorGroupboxSteps.setTitle(_translate("c", "Error"))
        self.yesErrorSteps.setText(_translate("c", "Yes"))
        self.noErrorSteps.setText(_translate("c", "No"))
        self.saveandNext.setText(_translate("c", "Save & Next"))
        self.cancelSteps.setText(_translate("c", "Cancel"))
        self.pushButton_2.setText(_translate("c", "Generate VRG"))
        self.pushButton_3.setText(_translate("c", "Cancel"))

    def close(self):
        QtWidgets.QWidget.close()

    def save_form_page(self):
        # print(self.formObj[0])
        self.formObj.set_formName(self.formName.text().lower())
        self.formObj.set_noOfSteps(self.noOfSteps.text())
        self.formObj.steps = []
        self.formGroupBox.setEnabled(False)
        self.stepGroupBox.setEnabled(True)
        if self.productCheckbox.isChecked():
            self.productGroupBoxSteps.setEnabled(True)
        else:
            self.productGroupBoxSteps.setEnabled(False)
        if self.transactionCheckbox.isChecked():
            self.transactionGroupBoxSteps.setEnabled(True)
        else:
            self.transactionGroupBoxSteps.setEnabled(False)

    def save_steps_information(self):
        noOfSteps = int(self.noOfSteps.text()) - 1
        stepsObj = StepsPage()
        self.step = ''
        if len(self.formObj.steps) == 0:
            stepsObj.set_stepName(self.stepNameTextbox.text())
            stepsObj.set_pageName(self.pageNameStepsTextbox.text())
            stepsObj.set_FromTransaction(self.formStepTextBox.text())
            stepsObj.set_ToTransaction(self.lineEdit_13.text())
            stepsObj.isExternal =  str(self.isExternalCheckbox.isChecked())

            stepsObj.set_formView(str(self.formView.isChecked()))
            stepsObj.set_formQualify(str(self.formQualify.isChecked()))
            stepsObj.set_formsubmit(str(self.formSubmit.isChecked()))
            stepsObj.set_formSteps('true')

            stepsObj.set_productId(self.productId.text())
            stepsObj.set_parentProduct(self.parentProduct.text())
            stepsObj.set_adjudication(self.adjudication.text())
            stepsObj.set_productPositioning(self.positioning_combobox.currentText())
            stepsObj.set_productGrouping(self.grouping_combobox.currentText())
            stepsObj.set_fulfillment(self.fulfillment_comboBox.currentText())

            if self.yesLoginSteps.isChecked() or self.bothLoginSteps.isChecked():
                stepsObj.set_UserId("{dynamic}")
                stepsObj.set_UserAuthState("{dynamic}")
                stepsObj.set_UserType("{dynamic}")
            if self.yesErrorSteps.isChecked():
                stepsObj.eventError = "true"
                stepsObj.errorMessage = "{dynamic}"
                stepsObj.errorsCode = "{dynamic}"
                stepsObj.errorsSubType = "{dynamic}"
                stepsObj.errorsType = "{dynamic}"
                stepsObj.errorsField = "{dynamic}"
            # if noOfSteps == len(self.formObj.steps):
            # self.stepGroupBox.setEnabled(False)
            self.step = json.dumps(stepsObj.__dict__)
            self.formObj.steps.append(json.loads(self.step))
        elif len(self.formObj.steps) < noOfSteps:
            stepsObj.set_stepName(self.stepNameTextbox.text())
            stepsObj.set_pageName(self.pageNameStepsTextbox.text())
            stepsObj.set_FromTransaction(self.formStepTextBox.text())
            stepsObj.set_ToTransaction(self.lineEdit_13.text())
            stepsObj.isExternal =  str(self.isExternalCheckbox.isChecked())

            stepsObj.set_formView(str(self.formView.isChecked()))
            stepsObj.set_formQualify(str(self.formQualify.isChecked()))
            stepsObj.set_formsubmit(str(self.formSubmit.isChecked()))
            stepsObj.set_formSteps('true')

            stepsObj.set_productId(self.productId.text())
            stepsObj.set_parentProduct(self.parentProduct.text())
            stepsObj.set_adjudication(self.adjudication.text())
            stepsObj.set_productPositioning(self.positioning_combobox.currentText())
            stepsObj.set_productGrouping(self.grouping_combobox.currentText())
            stepsObj.set_fulfillment(self.fulfillment_comboBox.currentText())

            if self.yesLoginSteps.isChecked() or self.bothLoginSteps.isChecked():
                stepsObj.set_UserId("{dynamic}")
                stepsObj.set_UserAuthState("{dynamic}")
                stepsObj.set_UserType("{dynamic}")
            if self.yesErrorSteps.isChecked():
                stepsObj.eventError = "true"
                stepsObj.errorMessage = "{dynamic}"
                stepsObj.errorsCode = "{dynamic}"
                stepsObj.errorsSubType = "{dynamic}"
                stepsObj.errorsType = "{dynamic}"
                stepsObj.errorsField = "{dynamic}"
            self.step = json.dumps(stepsObj.__dict__)
            self.formObj.steps.append(json.loads(self.step))
        else:
            stepsObj.set_stepName(self.stepNameTextbox.text())
            stepsObj.set_pageName(self.pageNameStepsTextbox.text())
            stepsObj.set_FromTransaction(self.formStepTextBox.text())
            stepsObj.set_ToTransaction(self.lineEdit_13.text())
            stepsObj.isExternal =  str(self.isExternalCheckbox.isChecked())

            stepsObj.set_formView(str(self.formView.isChecked()))
            stepsObj.set_formQualify(str(self.formQualify.isChecked()))
            stepsObj.set_formsubmit(str(self.formSubmit.isChecked()))
            stepsObj.set_formSteps('true')

            stepsObj.set_productId(self.productId.text())
            stepsObj.set_parentProduct(self.parentProduct.text())
            stepsObj.set_adjudication(self.adjudication.text())
            stepsObj.set_productPositioning(self.positioning_combobox.currentText())
            stepsObj.set_productGrouping(self.grouping_combobox.currentText())
            stepsObj.set_fulfillment(self.fulfillment_comboBox.currentText())

            if self.yesLoginSteps.isChecked() or self.bothLoginSteps.isChecked():
                stepsObj.set_UserId("{dynamic}")
                stepsObj.set_UserAuthState("{dynamic}")
                stepsObj.set_UserType("{dynamic}")
            if self.yesErrorSteps.isChecked():
                stepsObj.eventError = "true"
                stepsObj.errorMessage = "{dynamic}"
                stepsObj.errorsCode = "{dynamic}"
                stepsObj.errorsSubType = "{dynamic}"
                stepsObj.errorsType = "{dynamic}"
                stepsObj.errorsField = "{dynamic}"

            self.step = json.dumps(stepsObj.__dict__)
            self.formObj.steps.append(json.loads(self.step))
            form = json.dumps(self.formObj.__dict__)
            self.vrg.forms.append(json.loads(form))
            self.stepGroupBox.setEnabled(False)
            self.formName.setText('')
            self.noOfSteps.setText('')
            self.addFlow.setEnabled(True)
            self.addButton.setEnabled(True)
        self.clearResetFormFields()

    def clearResetFormFields(self):
        self.stepNameTextbox.setText('')
        self.pageNameStepsTextbox.setText('')
        self.formStepTextBox.setText('')
        self.lineEdit_13.setText('')

    def generatevrgdocument(self):
        obj = Vrg()
        self.vrg.set_ProjectName(self.projectName.text().lower())
        self.vrg.set_UserName(self.userName.text().lower())
        self.vrg.set_SiteName(str(self.siteName.text().lower()).lower().replace(" ", "-"))
        self.vrg.set_SiteBrand(self.brand_combobox.currentText().lower())
        self.vrg.set_ApplicationTypes(self.appliType_combo.currentText().lower())
        self.vrg.set_SiteType(self.comboBox.currentText().lower())
        obj = self.vrg
        json_page = json.dumps(obj.__dict__)
        app = AppVRG()
        val = json.loads(json_page)
        print(val)
        app.generate_VRG(val)

    def addFlow_Page(self):
        self.standAlonePageBox.setEnabled(False)
        self.formGroupBox.setEnabled(True)
        self.stepGroupBox.setEnabled(False)
        self.addButton.setEnabled(False)
        self.addFlow.setEnabled(False)

    def applicationType(self):
        if self.appliType_combo.currentText() == "Ember":
            self.pageName.setText("Route Name :")
        if self.appliType_combo.currentText() == "Angular":
            self.pageName.setText("Page Name :")
        if self.appliType_combo.currentText() == "Mobile JSON":
            self.pageName.setText("Page Name :")

    def siteType(self):
        if self.comboBox.currentText() == "Desktop":
            self.vrg.siteType = "desktop"
        if self.comboBox.currentText() == "Mobile":
            self.vrg.siteType = "mobile"
        if self.comboBox.currentText() == "Responsive":
            self.vrg.siteType = "responsive"

    def add_page_button(self):
        self.standAlonePageBox.setEnabled(True)
        self.formGroupBox.setEnabled(False)
        self.stepGroupBox.setEnabled(False)
        self.addButton.setEnabled(False)
        self.addFlow.setEnabled(False)

    def saveStandalonePage(self):
        # Pages Object
        obj1 = StandalonePage()
        obj1.set_pageName(str(self.pageName_2.text().replace(" ", "-")))
        obj1.set_pagePath(str(self.pageName_2.text().replace(" ", "-")))

        # Error Code Checked or Unchecked
        if (self.yes.isChecked()):
            obj1.eventError = "true"
            obj1.errorMessage = "{dynamic}"
            obj1.errorsCode = "{dynamic}"
            obj1.errorsType = "{dynamic}"
            obj1.errorsSubType = "{dynamic}"
            obj1.errorsField = "{dynamic}"

        # Login Code Checked or Unchecked
        if (self.yes_2.isChecked() or self.both.isChecked()):
            obj1.set_UserId("{dynamic}")
            obj1.set_UserAuthState("authenticated")
            obj1.set_UserType("{dynamic}")
        elif (self.no_2.isChecked()):
            obj1.set_UserId("")
            obj1.set_UserAuthState("non-authenticated")
            obj1.set_UserType("")

        page = json.dumps(obj1.__dict__)
        self.vrg.pages.append(json.loads(page))
        self.pageName_2.setText('')
        self.formStepTextBox.setText('')
        self.lineEdit_13.setText('')
        self.standAlonePageBox.setEnabled(False)
        self.addButton.setEnabled(True)
        self.addFlow.setEnabled(True)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    c = QtWidgets.QMainWindow()
    ui = Ui_c()
    ui.setupUi(c)
    c.show()
    sys.exit(app.exec_())
