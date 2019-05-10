"""
__author__ : Manish Apte
__maintainer__ : Manish  & karthik
__organization__ : Deloitte
"""

import json

from PyQt5 import QtCore, QtGui, QtWidgets

from Download import Download
from Form import Form
from GenerateVRG import GenerateVRG
from InteractionPage import InteractionPage
from StandalonePage import StandalonePage
from Steps import Steps
from Vrg import Vrg


class VRGAutomation(object):

    def __init__(self):
        self.vrg = Vrg()
        self.formObj = Form()

    def close(self):
        QtWidgets.QWidget.close(self)

    def save_form_page(self):
        self.formObj.set_form_name(self.formName.text().lower())
        self.formSteps.setChecked(True)
        self.formSteps.setEnabled(False)
        self.formObj.set_no_of_steps(self.noOfSteps.text())
        self.formObj.steps = []
        self.formGroupBox.setEnabled(False)
        self.stepGroupBox.setEnabled(True)
        if self.productCheckbox.isChecked():
            self.productGroupBoxSteps.setEnabled(True)
            self.formObj.is_product_exist = str(self.productCheckbox.isChecked())
        else:
            self.productGroupBoxSteps.setEnabled(False)
        if self.transactionCheckbox.isChecked():
            self.transactionGroupBoxSteps.setEnabled(True)
            self.formObj.is_transaction_exist = str(
                self.transactionCheckbox.isChecked())
        else:
            self.transactionGroupBoxSteps.setEnabled(False)

    def save_steps_information(self):
        noOfSteps = int(self.noOfSteps.text()) - 1
        stepsObj = Steps()
        self.step = ''
        if len(self.formObj.steps) == 0:
            stepsObj.set_step_name(self.stepNameTextbox.text())

            if self.appliType_combo.currentText() == "Ember":
                stepsObj.set_page_name(
                    str(self.pageHierSteps.text().lower().replace(" ", "-")))
                stepsObj.page_path = str(
                    self.pageHierSteps.text().lower().replace(" ", "-"))
                stepsObj.page_hierarchy = str(
                    self.pageHierSteps.text().lower().replace(" ", "-").split(
                        '.'))
            if self.appliType_combo.currentText() == "Angular" or \
                    self.appliType_combo.currentText() == "Mobile JSON":
                stepsObj.set_page_name(str(
                    self.pageNameStepsTextbox.text().lower().replace(" ",
                                                                     "-")))
                stepsObj.page_hierarchy = str(
                    self.pageHierSteps.text().lower().replace(" ", "-")).split(
                    '.')
                stepsObj.page_path = str(
                    self.pageNameStepsTextbox.text().lower().replace(" ", "-"))
            stepsObj.set_from_transaction(self.formStepTextBox.text())
            stepsObj.set_to_transaction(self.lineEdit_13.text())
            stepsObj.is_external = str(self.isExternalCheckbox.isChecked())

            stepsObj.set_form_view(str(self.formView.isChecked()).lower())
            stepsObj.set_form_qualify(str(self.formQualify.isChecked()).lower())
            stepsObj.set_form_submit(str(self.formSubmit.isChecked()).lower())
            stepsObj.set_form_step('true')

            stepsObj.set_product_id(
                str(self.productId.text()).lower().replace(" ", "-"))
            stepsObj.set_parent_product(
                str(self.parentProduct.text()).lower().replace(" ", "-"))
            stepsObj.set_adjudication(
                str(self.adjudication.text()).lower().replace(" ", "-"))

            if (str(
                    self.positioning_combobox.currentText()) != 'Not '
                                                                'Applicable'):
                stepsObj.set_product_positioning(str(
                    self.positioning_combobox.currentText()).lower().replace(
                    " ", "-"))
            if (str(self.grouping_combobox.currentText()) != 'Not Applicable'):
                stepsObj.set_product_grouping(
                    str(self.grouping_combobox.currentText()).lower().replace(
                        " ", "-"))
            if (str(
                    self.fulfillment_comboBox.currentText()) != 'Not '
                                                                'Applicable'):
                stepsObj.set_fulfillment(str(
                    self.fulfillment_comboBox.currentText()).lower().replace(
                    " ", "-"))
            stepsObj.set_is_paperless(str(self.isPaperless.isChecked()).lower())
            stepsObj.set_personal_details(
                str(self.personalDetails.isChecked()).lower())
            stepsObj.set_product_recommendation(
                str((self.productRecommendation.isChecked())).lower())
            stepsObj.set_summary(str(self.summary.isChecked()).lower())
            stepsObj.set_confirmation(
                str(self.confirmation.isChecked()).lower())
            stepsObj.set_terms_and_condition(
                str(self.termsandcondition.isChecked()).lower())

            if self.yesLoginSteps.isChecked() or \
                    self.bothLoginSteps.isChecked():
                stepsObj.set_user_id("{dynamic}")
                if self.yesLoginSteps.isChecked():
                    stepsObj.set_user_auth_state("authenticated")
                elif self.bothLoginSteps.isChecked():
                    stepsObj.set_user_auth_state("non-authenticated")
                stepsObj.set_user_type("{dynamic}")
            if self.yesErrorSteps.isChecked():
                stepsObj.event_error = "true"
                stepsObj.error_message = "{dynamic}"
                stepsObj.error_code = "{dynamic}"
                stepsObj.error_sub_type = "{dynamic}"
                stepsObj.error_type = "{dynamic}"
                stepsObj.error_field = "{dynamic}"
            if noOfSteps == len(self.formObj.steps):
                self.stepGroupBox.setEnabled(False)
            self.step = json.dumps(stepsObj.__dict__)
            self.formObj.steps.append(json.loads(self.step))
        elif len(self.formObj.steps) < noOfSteps:
            stepsObj.set_step_name(self.stepNameTextbox.text())
            if self.appliType_combo.currentText() == "Ember":
                stepsObj.set_page_name(
                    str(self.pageHierSteps.text().lower().replace(" ", "-")))
                stepsObj.page_path = str(
                    self.pageHierSteps.text().lower().replace(" ", "-"))
                stepsObj.page_hierarchy = str(
                    self.pageHierSteps.text().lower().replace(" ", "-").split(
                        '.'))
            if self.appliType_combo.currentText() == "Angular" or \
                    self.appliType_combo.currentText() == "Mobile JSON":
                stepsObj.set_page_name(str(
                    self.pageNameStepsTextbox.text().lower().replace(" ",
                                                                     "-")))
                stepsObj.page_hierarchy = str(
                    self.pageHierSteps.text().lower().replace(" ", "-").split(
                        '.'))

            stepsObj.set_from_transaction(self.formStepTextBox.text())
            stepsObj.set_to_transaction(self.lineEdit_13.text())
            stepsObj.is_external = str(self.isExternalCheckbox.isChecked())

            stepsObj.set_form_view(str(self.formView.isChecked()).lower())
            stepsObj.set_form_qualify(str(self.formQualify.isChecked()).lower())
            stepsObj.set_form_submit(str(self.formSubmit.isChecked()).lower())
            stepsObj.set_form_step('true')

            stepsObj.set_product_id(
                str(self.productId.text()).lower().replace(" ", "-"))
            stepsObj.set_parent_product(
                str(self.parentProduct.text()).lower().replace(" ", "-"))
            stepsObj.set_adjudication(
                str(self.adjudication.text()).lower().replace(" ", "-"))

            if (str(
                    self.positioning_combobox.currentText()) != 'Not '
                                                                'Applicable'):
                stepsObj.set_product_positioning(str(
                    self.positioning_combobox.currentText()).lower().replace(
                    " ", "-"))
            if (str(self.grouping_combobox.currentText()) != 'Not Applicable'):
                stepsObj.set_product_grouping(
                    str(self.grouping_combobox.currentText()).lower().replace(
                        " ", "-"))
            if (str(
                    self.fulfillment_comboBox.currentText()) != 'Not '
                                                                'Applicable'):
                stepsObj.set_fulfillment(str(
                    self.fulfillment_comboBox.currentText()).lower().replace(
                    " ", "-"))
            stepsObj.set_is_paperless(str(self.isPaperless.isChecked()).lower())
            stepsObj.set_personal_details(
                str(self.personalDetails.isChecked()).lower())
            stepsObj.set_product_recommendation(
                str((self.productRecommendation.isChecked())).lower())
            stepsObj.set_summary(str(self.summary.isChecked()).lower())
            stepsObj.set_confirmation(
                str(self.confirmation.isChecked()).lower())
            stepsObj.set_terms_and_condition(
                str(self.termsandcondition.isChecked()).lower())

            if self.yesLoginSteps.isChecked() or \
                    self.bothLoginSteps.isChecked():
                stepsObj.set_user_id("{dynamic}")
                if self.yesLoginSteps.isChecked():
                    stepsObj.set_user_auth_state("authenticated")
                elif self.bothLoginSteps.isChecked():
                    stepsObj.set_user_auth_state("non-authenticated")
                stepsObj.set_user_type("{dynamic}")
            if self.yesErrorSteps.isChecked():
                stepsObj.event_error = "true"
                stepsObj.error_message = "{dynamic}"
                stepsObj.error_code = "{dynamic}"
                stepsObj.error_sub_type = "{dynamic}"
                stepsObj.error_type = "{dynamic}"
                stepsObj.error_field = "{dynamic}"
            self.step = json.dumps(stepsObj.__dict__)
            self.formObj.steps.append(json.loads(self.step))
        else:
            stepsObj.set_step_name(self.stepNameTextbox.text())
            if self.appliType_combo.currentText() == "Ember":
                stepsObj.set_page_name(
                    str(self.pageHierSteps.text().lower().replace(" ", "-")))
                stepsObj.page_path = str(
                    self.pageHierSteps.text().lower().replace(" ", "-"))
                stepsObj.page_hierarchy = str(
                    self.pageHierSteps.text().lower().replace(" ", "-").split(
                        '.'))
            if self.appliType_combo.currentText() == "Angular" or \
                    self.appliType_combo.currentText() == "Mobile JSON":
                stepsObj.set_page_name(str(
                    self.pageNameStepsTextbox.text().lower().replace(" ",
                                                                     "-")))
                stepsObj.page_path = str(
                    self.pageNameStepsTextbox.text().lower().replace(" ", "-"))
                stepsObj.page_hierarchy = str(
                    self.pageHierSteps.text().lower().replace(" ", "-").split(
                        '.'))
            stepsObj.set_from_transaction(self.formStepTextBox.text())
            stepsObj.set_to_transaction(self.lineEdit_13.text())
            stepsObj.is_external = str(self.isExternalCheckbox.isChecked())

            stepsObj.set_form_view(str(self.formView.isChecked()).lower())
            stepsObj.set_form_qualify(str(self.formQualify.isChecked()).lower())
            stepsObj.set_form_submit(str(self.formSubmit.isChecked()).lower())
            stepsObj.set_form_step('true')

            stepsObj.set_product_id(
                str(self.productId.text()).lower().replace(" ", "-"))
            stepsObj.set_parent_product(
                str(self.parentProduct.text()).lower().replace(" ", "-"))
            stepsObj.set_adjudication(
                str(self.adjudication.text()).lower().replace(" ", "-"))

            if (str(
                    self.positioning_combobox.currentText()) != 'Not '
                                                                'Applicable'):
                stepsObj.set_product_positioning(str(
                    self.positioning_combobox.currentText()).lower().replace(
                    " ", "-"))

            if (str(self.grouping_combobox.currentText()) != 'Not Applicable'):
                stepsObj.set_product_grouping(
                    str(self.grouping_combobox.currentText()).lower().replace(
                        " ", "-"))

            if (str(
                    self.fulfillment_comboBox.currentText()) != 'Not '
                                                                'Applicable'):
                stepsObj.set_fulfillment(str(
                    self.fulfillment_comboBox.currentText()).lower().replace(
                    " ", "-"))

            stepsObj.set_is_paperless(str(self.isPaperless.isChecked()).lower())
            stepsObj.set_personal_details(
                str(self.personalDetails.isChecked()).lower())
            stepsObj.set_product_recommendation(
                str((self.productRecommendation.isChecked())).lower())
            stepsObj.set_summary(str(self.summary.isChecked()).lower())
            stepsObj.set_confirmation(
                str(self.confirmation.isChecked()).lower())
            stepsObj.set_terms_and_condition(
                str(self.termsandcondition.isChecked()).lower())
            if self.yesLoginSteps.isChecked() or \
                    self.bothLoginSteps.isChecked():
                stepsObj.set_user_id("{dynamic}")
                stepsObj.set_user_auth_state("authenticated")
                stepsObj.set_user_type("{dynamic}")
            if self.yesErrorSteps.isChecked():
                stepsObj.event_error = "true"
                stepsObj.error_message = "{dynamic}"
                stepsObj.error_code = "{dynamic}"
                stepsObj.error_sub_type = "{dynamic}"
                stepsObj.error_type = "{dynamic}"
                stepsObj.error_field = "{dynamic}"

            self.step = json.dumps(stepsObj.__dict__)
            self.formObj.steps.append(json.loads(self.step))
            form = json.dumps(self.formObj.__dict__)
            self.vrg.forms.append(json.loads(form))
            self.clearFormDetails()
        self.clearResetFormFields()

    def clearFormDetails(self):
        self.stepGroupBox.setEnabled(False)
        self.formName.setText('')
        self.noOfSteps.setText('')
        self.addFlow.setEnabled(True)
        self.addButton.setEnabled(True)
        self.interButton.setEnabled(True)
        self.downloadButton.setEnabled(True)
        self.productId.setText('')
        self.parentProduct.setText('')
        self.adjudication.setText('')
        self.fulfillment_comboBox.setCurrentIndex(0)
        self.grouping_combobox.setCurrentIndex(0)
        self.positioning_combobox.setCurrentIndex(0)

    def clearResetFormFields(self):
        self.stepNameTextbox.setText('')
        self.pageNameStepsTextbox.setText('')
        self.pageHierSteps.setText('')
        self.formStepTextBox.setText('')
        self.lineEdit_13.setText('')
        self.yesLoginSteps.setChecked(False)
        self.bothLoginSteps.setChecked(False)
        self.nologinSteps.setChecked(False)
        self.isPaperless.setChecked(False)
        self.personalDetails.setChecked(False)
        self.productRecommendation.setChecked(False)
        self.summary.setChecked(False)
        self.confirmation.setChecked(False)
        self.termsandcondition.setChecked(False)

    def generateVrgDocument(self):
        obj = Vrg()
        self.vrg.set_project_name(
            self.projectName.text().lower().replace(" ", "-"))
        self.vrg.set_user_name(self.userName.text().lower())
        self.vrg.set_site_name(self.siteName.text().lower().replace(" ", "-"))
        self.vrg.set_site_brand(
            self.brand_combobox.currentText().lower().replace(" ", "-"))
        self.vrg.set_application_types(
            self.appliType_combo.currentText().lower().replace(" ", "-"))
        self.vrg.set_SiteType(
            self.comboBox.currentText().lower().replace(" ", "-"))
        obj = self.vrg
        json_page = json.dumps(obj.__dict__)
        app = GenerateVRG()
        val = json.loads(json_page)
        app.generate_VRG(val)

    def addFlow_Page(self):
        self.standAlonePageBox.setEnabled(False)
        self.formGroupBox.setEnabled(True)
        self.stepGroupBox.setEnabled(False)
        self.addButton.setEnabled(False)
        self.addFlow.setEnabled(False)
        self.downloadButton.setEnabled(False)
        self.interButton.setEnabled(False)

    def applicationType(self):
        if self.appliType_combo.currentText() == "Ember":
            self.pageName.setText("Page Name :")
            self.pageHierLabel.setText("Route Name:")
            self.pageNameLabelSteps.setText("Page Name")
            self.pageHierLabelSteps.setText("Route Name")
            self.pageName_2.setEnabled(False)
            self.pageNameStepsTextbox.setEnabled(False)
        if self.appliType_combo.currentText() == "Angular":
            self.pageName.setText("Page Name :")
            self.pageHierLabel.setText("Page Hierarchy : ")
            self.pageNameLabelSteps.setText("Page Name : ")
            self.pageHierLabelSteps.setText("Page Hierarchy : ")
            self.pageName_2.setEnabled(True)
            self.pageNameStepsTextbox.setEnabled(True)
        if self.appliType_combo.currentText() == "Mobile JSON":
            self.pageName.setText("Page Name :")
            self.pageHierLabel.setText("Page Hierarchy : ")
            self.pageNameLabelSteps.setText("Page Name : ")
            self.pageHierLabelSteps.setText("Page Hierarchy : ")

    def siteType(self):
        if self.comboBox.currentText() == "Desktop":
            self.vrg.site_type = "desktop"
        if self.comboBox.currentText() == "Mobile":
            self.vrg.site_type = "mobile"
        if self.comboBox.currentText() == "Responsive":
            self.vrg.site_type = "responsive"

    def add_page_button(self):
        self.standAlonePageBox.setEnabled(True)
        self.formGroupBox.setEnabled(False)
        self.stepGroupBox.setEnabled(False)
        self.addButton.setEnabled(False)
        self.addFlow.setEnabled(False)
        self.InterGroupBox.setEnabled(False)
        self.DownloadGroupBox.setEnabled(False)

    def interButton_Page(self):
        self.InterGroupBox.setEnabled(True)
        self.standAlonePageBox.setEnabled(False)
        self.formGroupBox.setEnabled(False)
        self.stepGroupBox.setEnabled(False)
        self.addButton.setEnabled(False)
        self.addFlow.setEnabled(False)
        self.interButton.setEnabled(False)
        self.downloadButton.setEnabled(False)

    def downloadButton_Page(self):
        self.DownloadGroupBox.setEnabled(True)
        self.standAlonePageBox.setEnabled(False)
        self.formGroupBox.setEnabled(False)
        self.stepGroupBox.setEnabled(False)
        self.addButton.setEnabled(False)
        self.addFlow.setEnabled(False)
        self.interButton.setEnabled(False)
        self.downloadButton.setEnabled(False)
        self.InterGroupBox.setEnabled(False)

    def saveDownloadInfo(self):
        obj = Download()
        obj.download_file_name = str(
            self.downName.text().lower().replace(" ", "-"))
        obj.download_file_type = str(
            self.downTypeCB.currentText().lower().replace(" ", "-"))
        downloadSection = json.dumps(obj.__dict__)

        self.vrg.download.append(json.loads(downloadSection))
        self.downName.setText('')
        self.downTypeCB.setCurrentIndex(0)
        self.DownloadGroupBox.setEnabled(False)
        self.addButton.setEnabled(True)
        self.interButton.setEnabled(True)
        self.downloadButton.setEnabled(True)
        self.addFlow.setEnabled(True)

    def saveInterInfo(self):
        obj_interaction = InteractionPage()
        obj_interaction.site_interaction_event = "true"
        obj_interaction.interaction_name = self.interName.text()
        interactionAction = json.dumps(obj_interaction.__dict__)

        self.vrg.interaction.append(json.loads(interactionAction))
        self.interName.setText('')

        self.InterGroupBox.setEnabled(False)
        self.addButton.setEnabled(True)
        self.interButton.setEnabled(True)
        self.downloadButton.setEnabled(True)
        self.addFlow.setEnabled(True)

    def saveStandalonePage(self):
        obj1 = StandalonePage()
        if self.appliType_combo.currentText() == "Ember":
            obj1.set_page_name(
                str(self.pageHier.text().lower().replace(" ", "-")))
            obj1.set_page_path(
                str(self.pageHier.text().lower().replace(" ", "-")))
            obj1.page_hierarchy = str(
                self.pageHier.text().lower().replace(" ", "-").split('.'))
        if self.appliType_combo.currentText() == "Angular" or \
                self.appliType_combo.currentText() == "Mobile JSON":
            obj1.set_page_name(
                str(self.pageName_2.text().lower().replace(" ", "-")))
            obj1.page_hierarchy = str(
                self.pageHier.text().lower().replace(" ", "-").split('.'))
            obj1.set_page_path(
                str(self.pageName_2.text().lower().replace(" ", "-")))

        if (self.yes.isChecked()):
            obj1.event_error = "true"
            obj1.error_message = "{dynamic}"
            obj1.error_code = "{dynamic}"
            obj1.error_type = "{dynamic}"
            obj1.error_sub_type = "{dynamic}"
            obj1.error_field = "{dynamic}"

        # Login Code Checked or Unchecked
        if (self.yes_2.isChecked() or self.both.isChecked()):
            obj1.set_user_id("{dynamic}")
            obj1.set_user_auth_state("authenticated")
            obj1.set_user_type("{dynamic}")
            obj1.login_event = "true"
        elif (self.no_2.isChecked()):
            obj1.set_user_id("")
            obj1.set_user_auth_state("non-authenticated")
            obj1.set_user_type("")

        page = json.dumps(obj1.__dict__)
        self.vrg.pages.append(json.loads(page))
        self.pageName_2.setText('')
        self.formStepTextBox.setText('')
        self.pageHier.setText('')
        self.lineEdit_13.setText('')
        self.standAlonePageBox.setEnabled(False)
        self.addButton.setEnabled(True)
        self.addFlow.setEnabled(True)

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
        self.label.setGeometry(QtCore.QRect(380, 30, 500, 31))

        self.projectName_label = QtWidgets.QLabel(self.centralwidget)
        self.projectName_label.setGeometry(QtCore.QRect(20, 70, 101, 28))
        self.projectName_label.setObjectName("projectName_label")

        self.projectName = QtWidgets.QLineEdit(self.centralwidget)
        self.projectName.setGeometry(QtCore.QRect(150, 70, 231, 28))
        self.projectName.setObjectName("projectName")

        self.userName_label = QtWidgets.QLabel(self.centralwidget)
        self.userName_label.setGeometry(QtCore.QRect(490, 70, 90, 28))
        self.userName_label.setObjectName("userName_label")

        self.userName = QtWidgets.QLineEdit(self.centralwidget)
        self.userName.setGeometry(QtCore.QRect(620, 70, 241, 28))
        self.userName.setObjectName("user_name")
        self.userName.setText(os.getlogin())
        self.userName.setEnabled(False)

        self.brand_label = QtWidgets.QLabel(self.centralwidget)
        self.brand_label.setGeometry(QtCore.QRect(20, 130, 55, 28))
        self.brand_label.setObjectName("brand_label")

        self.brand_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.brand_combobox.setGeometry(QtCore.QRect(150, 130, 241, 28))
        self.brand_combobox.setObjectName("brand_combobox")
        self.brand_combobox.addItem("")
        self.brand_combobox.setItemText(0, "")
        self.brand_combobox.addItem("")
        self.brand_combobox.addItem("")
        self.brand_combobox.addItem("")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(490, 130, 125, 28))
        self.label_6.setObjectName("label_6")

        self.appliType_combo = QtWidgets.QComboBox(self.centralwidget)
        self.appliType_combo.setGeometry(QtCore.QRect(620, 130, 241, 28))
        self.appliType_combo.setObjectName("appliType_combo")
        self.appliType_combo.addItem("")
        self.appliType_combo.setItemText(0, "")
        self.appliType_combo.addItem("")
        self.appliType_combo.addItem("")
        self.appliType_combo.addItem("")
        self.appliType_combo.currentIndexChanged.connect(self.applicationType)

        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(100, 240, 93, 28))
        self.addButton.setObjectName("addButton")
        self.addButton.clicked.connect(self.add_page_button)

        self.addFlow = QtWidgets.QPushButton(self.centralwidget)
        self.addFlow.setGeometry(QtCore.QRect(250, 240, 93, 28))
        self.addFlow.setObjectName("addFlow")
        self.addFlow.clicked.connect(self.addFlow_Page)

        self.downloadButton = QtWidgets.QPushButton(self.centralwidget)
        self.downloadButton.setGeometry(QtCore.QRect(400, 240, 93, 28))
        self.downloadButton.setObjectName("downloadButton")
        self.downloadButton.clicked.connect(self.downloadButton_Page)

        self.interButton = QtWidgets.QPushButton(self.centralwidget)
        self.interButton.setGeometry(QtCore.QRect(550, 240, 93, 28))
        self.interButton.setObjectName("addFlow")
        self.interButton.clicked.connect(self.interButton_Page)

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(60, 370, 55, 16))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")

        self.standAlonePageBox = QtWidgets.QGroupBox(self.centralwidget)
        self.standAlonePageBox.setGeometry(QtCore.QRect(30, 290, 421, 351))
        self.standAlonePageBox.setObjectName("standAlonePageBox")

        self.pageName = QtWidgets.QLabel(self.standAlonePageBox)
        self.pageName.setGeometry(QtCore.QRect(50, 40, 91, 28))
        self.pageName.setObjectName("page_name")

        self.pageName_2 = QtWidgets.QLineEdit(self.standAlonePageBox)
        self.pageName_2.setGeometry(QtCore.QRect(185, 40, 191, 28))
        self.pageName_2.setObjectName("pageName_2")

        self.pageHierLabel = QtWidgets.QLabel(self.standAlonePageBox)
        self.pageHierLabel.setGeometry(QtCore.QRect(50, 80, 115, 28))
        self.pageHierLabel.setObjectName("pageHierLabel")

        self.pageHier = QtWidgets.QLineEdit(self.standAlonePageBox)
        self.pageHier.setGeometry(QtCore.QRect(185, 80, 191, 28))
        self.pageHier.setObjectName("pageHier")

        self.errorGroupBoxPage = QtWidgets.QGroupBox(self.standAlonePageBox)
        self.errorGroupBoxPage.setGeometry(QtCore.QRect(50, 115, 291, 61))
        self.errorGroupBoxPage.setObjectName("errorGroupBoxPage")

        self.yes = QtWidgets.QRadioButton(self.errorGroupBoxPage)
        self.yes.setGeometry(QtCore.QRect(70, 20, 95, 20))
        self.yes.setObjectName("yes")

        self.no = QtWidgets.QRadioButton(self.errorGroupBoxPage)
        self.no.setGeometry(QtCore.QRect(140, 20, 95, 20))
        self.no.setObjectName("no")

        self.loginGroupBoxPage = QtWidgets.QGroupBox(self.standAlonePageBox)
        self.loginGroupBoxPage.setGeometry(QtCore.QRect(50, 180, 291, 80))
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
        self.saveButton.setGeometry(QtCore.QRect(50, 290, 93, 28))
        self.saveButton.setObjectName("saveButton")
        self.saveButton.clicked.connect(self.saveStandalonePage)

        self.cancelButton = QtWidgets.QPushButton(self.standAlonePageBox)
        self.cancelButton.setGeometry(QtCore.QRect(200, 290, 93, 28))
        self.cancelButton.setObjectName("cancelButton")

        self.standAlonePageBox.setEnabled(False)

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(150, 180, 241, 28))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.currentIndexChanged.connect(self.siteType)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 180, 81, 28))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(490, 180, 81, 28))
        self.label_3.setObjectName("label_3")
        self.siteName = QtWidgets.QLineEdit(self.centralwidget)
        self.siteName.setGeometry(QtCore.QRect(620, 180, 241, 28))
        self.siteName.setObjectName("site_name")
        self.formGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.formGroupBox.setGeometry(QtCore.QRect(460, 290, 411, 351))
        self.formGroupBox.setObjectName("formGroupBox")
        self.label_4 = QtWidgets.QLabel(self.formGroupBox)
        self.label_4.setGeometry(QtCore.QRect(30, 50, 91, 28))
        self.label_4.setObjectName("label_4")
        self.formName = QtWidgets.QLineEdit(self.formGroupBox)
        self.formName.setGeometry(QtCore.QRect(150, 50, 201, 28))
        self.formName.setObjectName("form_name")
        self.label_5 = QtWidgets.QLabel(self.formGroupBox)
        self.label_5.setGeometry(QtCore.QRect(40, 130, 91, 28))
        self.label_5.setObjectName("label_5")
        self.noOfSteps = QtWidgets.QLineEdit(self.formGroupBox)
        self.noOfSteps.setGeometry(QtCore.QRect(150, 120, 201, 28))
        self.noOfSteps.setObjectName("no_of_steps")
        self.productCheckbox = QtWidgets.QCheckBox(self.formGroupBox)
        self.productCheckbox.setGeometry(QtCore.QRect(50, 200, 81, 20))
        self.productCheckbox.setObjectName("productCheckbox")
        self.transactionCheckbox = QtWidgets.QCheckBox(self.formGroupBox)
        self.transactionCheckbox.setGeometry(QtCore.QRect(160, 200, 111, 20))
        self.transactionCheckbox.setObjectName("transactionCheckbox")
        # self.dsr = QtWidgets.QCheckBox(self.formGroupBox)
        # self.dsr.setGeometry(QtCore.QRect(290, 200, 81, 20))
        # self.dsr.setObjectName("dsr")
        self.generateSteps = QtWidgets.QPushButton(self.formGroupBox)
        self.generateSteps.setGeometry(QtCore.QRect(120, 260, 121, 28))
        self.generateSteps.setObjectName("generateSteps")
        self.generateSteps.clicked.connect(self.save_form_page)
        self.formGroupBox.setEnabled(False)

        self.stepGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.stepGroupBox.setGeometry(QtCore.QRect(890, 20, 1001, 791))
        self.stepGroupBox.setObjectName("stepGroupBox")
        self.pageNameLabelSteps = QtWidgets.QLabel(self.stepGroupBox)
        self.pageNameLabelSteps.setGeometry(QtCore.QRect(50, 40, 91, 28))
        self.pageNameLabelSteps.setObjectName("pageNameLabelSteps")
        self.pageNameStepsTextbox = QtWidgets.QLineEdit(self.stepGroupBox)
        self.pageNameStepsTextbox.setGeometry(QtCore.QRect(140, 40, 181, 28))
        self.pageNameStepsTextbox.setObjectName("pageNameStepsTextbox")

        self.stepNameLabel = QtWidgets.QLabel(self.stepGroupBox)
        self.stepNameLabel.setGeometry(QtCore.QRect(520, 30, 115, 28))
        self.stepNameLabel.setObjectName("stepNameLabel")

        self.stepNameTextbox = QtWidgets.QLineEdit(self.stepGroupBox)
        self.stepNameTextbox.setGeometry(QtCore.QRect(640, 30, 200, 28))
        self.stepNameTextbox.setObjectName("stepNameTextbox")

        self.pageHierLabelSteps = QtWidgets.QLabel(self.stepGroupBox)
        self.pageHierLabelSteps.setGeometry(QtCore.QRect(520, 80, 115, 28))
        self.pageHierLabelSteps.setObjectName("pageHierLabelSteps")

        self.pageHierSteps = QtWidgets.QLineEdit(self.stepGroupBox)
        self.pageHierSteps.setGeometry(QtCore.QRect(640, 80, 200, 28))
        self.pageHierSteps.setObjectName("pageHierSteps")

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
        self.formView.setObjectName("form_view")
        self.formSubmit = QtWidgets.QCheckBox(self.formGroupBoxSteps)
        self.formSubmit.setGeometry(QtCore.QRect(130, 60, 121, 20))
        self.formSubmit.setObjectName("form_submit")
        self.formQualify = QtWidgets.QCheckBox(self.formGroupBoxSteps)
        self.formQualify.setGeometry(QtCore.QRect(390, 20, 161, 20))
        self.formQualify.setObjectName("form_qualify")
        self.formSteps = QtWidgets.QCheckBox(self.formGroupBoxSteps)
        self.formSteps.setGeometry(QtCore.QRect(390, 60, 101, 20))
        self.formSteps.setObjectName("form_steps")
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
        self.productAppGroupboxSteps = QtWidgets.QGroupBox(
            self.productGroupBoxSteps)
        self.productAppGroupboxSteps.setGeometry(
            QtCore.QRect(30, 140, 891, 131))
        self.productAppGroupboxSteps.setObjectName("productAppGroupboxSteps")
        self.personalDetails = QtWidgets.QCheckBox(
            self.productAppGroupboxSteps)
        self.personalDetails.setGeometry(QtCore.QRect(100, 30, 171, 20))
        self.personalDetails.setObjectName("personal_details")
        self.summary = QtWidgets.QCheckBox(self.productAppGroupboxSteps)
        self.summary.setGeometry(QtCore.QRect(340, 30, 120, 21))
        self.summary.setObjectName("summary")
        self.confirmation = QtWidgets.QCheckBox(self.productAppGroupboxSteps)
        self.confirmation.setGeometry(QtCore.QRect(550, 30, 131, 20))
        self.confirmation.setObjectName("confirmation")
        self.productRecommendation = QtWidgets.QCheckBox(
            self.productAppGroupboxSteps)
        self.productRecommendation.setGeometry(QtCore.QRect(100, 60, 171, 20))
        self.productRecommendation.setObjectName("product_recommendation")
        self.termsandcondition = QtWidgets.QCheckBox(
            self.productAppGroupboxSteps)
        self.termsandcondition.setGeometry(QtCore.QRect(340, 60, 180, 20))
        self.termsandcondition.setObjectName("termsandcondition")
        self.isPaperless = QtWidgets.QCheckBox(self.productAppGroupboxSteps)
        self.isPaperless.setGeometry(QtCore.QRect(550, 60, 131, 20))
        self.isPaperless.setObjectName("is_paperless")
        self.productIdLabel = QtWidgets.QLabel(self.productGroupBoxSteps)
        self.productIdLabel.setGeometry(QtCore.QRect(10, 40, 91, 28))
        self.productIdLabel.setObjectName("productIdLabel")
        self.productId = QtWidgets.QLineEdit(self.productGroupBoxSteps)
        self.productId.setGeometry(QtCore.QRect(110, 40, 161, 28))
        self.productId.setObjectName("product_id")
        self.parentProductLabel = QtWidgets.QLabel(self.productGroupBoxSteps)
        self.parentProductLabel.setGeometry(QtCore.QRect(300, 40, 121, 28))
        self.parentProductLabel.setObjectName("parentProductLabel")
        self.parentProduct = QtWidgets.QLineEdit(self.productGroupBoxSteps)
        self.parentProduct.setGeometry(QtCore.QRect(430, 40, 181, 28))
        self.parentProduct.setObjectName("parent_product")
        self.adJudicationLabel = QtWidgets.QLabel(self.productGroupBoxSteps)
        self.adJudicationLabel.setGeometry(QtCore.QRect(640, 40, 130, 28))
        self.adJudicationLabel.setObjectName("adJudicationLabel")
        self.adjudication = QtWidgets.QLineEdit(self.productGroupBoxSteps)
        self.adjudication.setGeometry(QtCore.QRect(740, 40, 181, 28))
        self.adjudication.setObjectName("adjudication")
        self.positioningLabel = QtWidgets.QLabel(self.productGroupBoxSteps)
        self.positioningLabel.setGeometry(QtCore.QRect(10, 90, 111, 28))
        self.positioningLabel.setObjectName("positioningLabel")
        self.positioning_combobox = QtWidgets.QComboBox(
            self.productGroupBoxSteps)
        self.positioning_combobox.setGeometry(QtCore.QRect(110, 90, 161, 28))
        self.positioning_combobox.setObjectName("positioning_combobox")
        self.positioning_combobox.addItem("")
        self.positioning_combobox.addItem("")
        self.positioning_combobox.addItem("")
        self.positioning_combobox.addItem("")
        self.positioning_combobox.addItem("")
        self.positioning_combobox.addItem("")
        self.groupingLabel = QtWidgets.QLabel(self.productGroupBoxSteps)
        self.groupingLabel.setGeometry(QtCore.QRect(300, 90, 160, 28))
        self.groupingLabel.setObjectName("groupingLabel")
        self.grouping_combobox = QtWidgets.QComboBox(self.productGroupBoxSteps)
        self.grouping_combobox.setGeometry(QtCore.QRect(430, 90, 181, 28))
        self.grouping_combobox.setObjectName("grouping_combobox")
        self.grouping_combobox.addItem("")
        self.grouping_combobox.addItem("")
        self.grouping_combobox.addItem("")
        self.grouping_combobox.addItem("")
        self.fulfillmentLabel = QtWidgets.QLabel(self.productGroupBoxSteps)
        self.fulfillmentLabel.setGeometry(QtCore.QRect(640, 90, 180, 28))
        self.fulfillmentLabel.setObjectName("fulfillmentLabel")
        self.fulfillment_comboBox = QtWidgets.QComboBox(
            self.productGroupBoxSteps)
        self.fulfillment_comboBox.setGeometry(QtCore.QRect(740, 90, 180, 28))
        self.fulfillment_comboBox.setObjectName("fulfillment_comboBox")
        self.fulfillment_comboBox.addItem("")
        self.fulfillment_comboBox.addItem("")
        self.fulfillment_comboBox.addItem("")
        self.fulfillment_comboBox.addItem("")
        self.fulfillment_comboBox.addItem("")
        self.fulfillment_comboBox.addItem("")
        self.transactionGroupBoxSteps = QtWidgets.QGroupBox(self.stepGroupBox)
        self.transactionGroupBoxSteps.setGeometry(
            QtCore.QRect(50, 190, 351, 191))
        self.transactionGroupBoxSteps.setObjectName("transactionGroupBoxSteps")
        self.formStepsLabel = QtWidgets.QLabel(self.transactionGroupBoxSteps)
        self.formStepsLabel.setGeometry(QtCore.QRect(40, 40, 55, 28))
        self.formStepsLabel.setObjectName("formStepsLabel")
        self.formStepTextBox = QtWidgets.QLineEdit(
            self.transactionGroupBoxSteps)
        self.formStepTextBox.setGeometry(QtCore.QRect(130, 40, 151, 28))
        self.formStepTextBox.setObjectName("formStepTextBox")
        self.toStepsLabel = QtWidgets.QLabel(self.transactionGroupBoxSteps)
        self.toStepsLabel.setGeometry(QtCore.QRect(30, 90, 55, 28))
        self.toStepsLabel.setObjectName("toStepsLabel")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.transactionGroupBoxSteps)
        self.lineEdit_13.setGeometry(QtCore.QRect(130, 90, 151, 28))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.isExternalCheckbox = QtWidgets.QCheckBox(
            self.transactionGroupBoxSteps)
        self.isExternalCheckbox.setGeometry(QtCore.QRect(130, 140, 141, 20))
        self.isExternalCheckbox.setObjectName("isExternalCheckbox")
        self.errorGroupboxSteps = QtWidgets.QGroupBox(self.stepGroupBox)
        self.errorGroupboxSteps.setGeometry(QtCore.QRect(510, 110, 411, 101))
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

        self.DownloadGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.DownloadGroupBox.setGeometry(QtCore.QRect(40, 650, 400, 190))
        self.DownloadGroupBox.setObjectName("DownGroupBox")

        self.downLabel = QtWidgets.QLabel(self.DownloadGroupBox)
        self.downLabel.setGeometry(QtCore.QRect(30, 50, 130, 28))
        self.downLabel.setObjectName("downLabel")

        self.downName = QtWidgets.QLineEdit(self.DownloadGroupBox)
        self.downName.setGeometry(QtCore.QRect(160, 50, 180, 28))
        self.downName.setObjectName("downName")

        self.downTypeLabel = QtWidgets.QLabel(self.DownloadGroupBox)
        self.downTypeLabel.setGeometry(QtCore.QRect(30, 100, 180, 28))
        self.downTypeLabel.setObjectName("downTypeLabel")

        self.downTypeCB = QtWidgets.QComboBox(self.DownloadGroupBox)
        self.downTypeCB.setGeometry(QtCore.QRect(160, 100, 180, 28))
        self.downTypeCB.setObjectName("downTypeCB")
        self.downTypeCB.addItem("")
        self.downTypeCB.addItem("")
        self.downTypeCB.addItem("")
        self.downTypeCB.addItem("")

        self.downloadSaveButton = QtWidgets.QPushButton(self.DownloadGroupBox)
        self.downloadSaveButton.setGeometry(QtCore.QRect(180, 150, 93, 28))
        self.downloadSaveButton.setObjectName("savedown")
        self.downloadSaveButton.clicked.connect(self.saveDownloadInfo)

        self.DownloadGroupBox.setEnabled(False)

        self.InterGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.InterGroupBox.setGeometry(QtCore.QRect(450, 650, 400, 190))
        self.InterGroupBox.setObjectName("InterGroupBox")

        self.interLabel = QtWidgets.QLabel(self.InterGroupBox)
        self.interLabel.setGeometry(QtCore.QRect(30, 50, 130, 28))
        self.interLabel.setObjectName("interLabel")

        self.interName = QtWidgets.QLineEdit(self.InterGroupBox)
        self.interName.setGeometry(QtCore.QRect(160, 50, 180, 28))
        self.interName.setObjectName("interName")

        self.interSaveButton = QtWidgets.QPushButton(self.InterGroupBox)
        self.interSaveButton.setGeometry(QtCore.QRect(180, 150, 100, 28))
        self.interSaveButton.setObjectName("saveinter")
        self.interSaveButton.clicked.connect(self.saveInterInfo)

        self.InterGroupBox.setEnabled(False)

        # self.ListGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        # self.ListGroupBox.setGeometry(QtCore.QRect(40, 900, 400, 100))
        # self.ListGroupBox.setObjectName("ListGroupBox")

        # self.lstGroupBox = QtWidgets.QListWidget(self.ListGroupBox)
        # self.lstGroupBox.setGeometry(QtCore.QRect(30, 50, 130, 28))
        # self.lstGroupBox.setObjectName("lstGroupBox")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 900, 120, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.generateVrgDocument)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(380, 900, 120, 28))
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
        c.setWindowTitle(_translate("c", "CIBC VRG Automation"))
        self.label.setText(_translate("c", "       VRG Automation"))
        self.projectName_label.setText(_translate("c", "Project Name:"))
        self.userName_label.setText(_translate("c", "Prepared By: "))
        self.brand_label.setText(_translate("c", "Brand :"))
        self.brand_combobox.setItemText(1, _translate("c", "CIBC"))
        self.brand_combobox.setItemText(2, _translate("c", "CIBC US"))
        self.brand_combobox.setItemText(3, _translate("c", "SIMPLII"))
        self.label_6.setText(_translate("c", "Application Type:"))
        self.appliType_combo.setItemText(1, _translate("c", "Ember"))
        self.appliType_combo.setItemText(2, _translate("c", "Angular"))
        self.appliType_combo.setItemText(3, _translate("c", "Mobile JSON"))

        self.addButton.setText(_translate("c", "Add Page"))
        self.addFlow.setText(_translate("c", "Add Flow"))
        self.downloadButton.setText(_translate("c", " Add Download"))
        self.interButton.setText(_translate("c", "Add Interaction"))

        self.standAlonePageBox.setTitle(_translate("c", "StandAlone Page"))
        self.pageName.setText(_translate("c", "Page Name:"))
        self.pageHierLabel.setText(_translate("c", "Page Hierarchy:"))
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
        self.formGroupBox.setTitle(_translate("c", "Form Flow"))
        self.label_4.setText(_translate("c", "Form Name :"))
        self.label_5.setText(_translate("c", "No. Of Steps : "))
        self.productCheckbox.setText(_translate("c", "Products"))
        self.transactionCheckbox.setText(_translate("c", "Transaction"))
        # self.dsr.setText(_translate("c", "DSR"))
        self.generateSteps.setText(_translate("c", "Generate Steps"))
        self.stepGroupBox.setTitle(_translate("c", "Steps"))
        self.pageNameLabelSteps.setText(_translate("c", "Page Name:"))
        self.stepNameLabel.setText(_translate("c", "Step Name:"))
        self.pageHierLabelSteps.setText(_translate("c", "Page Hierarchy:"))
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
        self.productGroupBoxSteps.setTitle(
            _translate("c", "Product Information"))
        self.productAppGroupboxSteps.setTitle(
            _translate("c", "Product Application Steps"))
        self.personalDetails.setText(_translate("c", "Personal Details"))
        self.summary.setText(_translate("c", "Summary"))
        self.confirmation.setText(_translate("c", "Confirmation"))
        self.productRecommendation.setText(
            _translate("c", "Product Recommendation"))
        self.termsandcondition.setText(_translate("c", "Terms and Condition"))
        self.isPaperless.setText(_translate("c", "Is Paperless"))
        self.productIdLabel.setText(_translate("c", "Product Id :"))
        self.parentProductLabel.setText(_translate("c", "Parent Product"))
        self.adJudicationLabel.setText(_translate("c", "Adjudication:"))
        self.positioningLabel.setText(_translate("c", "Postioning:"))
        self.positioning_combobox.setItemText(0,
                                              _translate("c",
                                                         "Not Applicable"))
        self.positioning_combobox.setItemText(1, _translate("c", "Upsell"))
        self.positioning_combobox.setItemText(2, _translate("c", "downsell"))
        self.positioning_combobox.setItemText(3,
                                              _translate("c", "user selected"))
        self.positioning_combobox.setItemText(4, _translate("c",
                                                            "system "
                                                            "recommended"))
        self.positioning_combobox.setItemText(5, _translate("c", "Dynamic"))
        self.groupingLabel.setText(_translate("c", "Grouping:"))
        self.grouping_combobox.setItemText(0,
                                           _translate("c", "Not Applicable"))
        self.grouping_combobox.setItemText(1, _translate("c", "Bundle Id"))
        self.grouping_combobox.setItemText(2, _translate("c", "No Grouping"))
        self.grouping_combobox.setItemText(3, _translate("c", "Dynamic"))
        self.fulfillmentLabel.setText(_translate("c", "Fulfillment:"))
        self.fulfillment_comboBox.setItemText(0,
                                              _translate("c",
                                                         "Not Applicable"))
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
        # self.ListGroupBox.setTitle(_translate("c", "ListGroup"))

        self.DownloadGroupBox.setTitle(_translate("c", "Download"))
        self.downTypeLabel.setText(_translate("c", "File Type :"))

        self.downTypeCB.setItemText(0, _translate("c", ""))
        self.downTypeCB.setItemText(1, _translate("c", "PDF"))
        self.downTypeCB.setItemText(2, _translate("c", "JPEG"))
        self.downTypeCB.setItemText(3, _translate("c", "OTHER"))

        self.downLabel.setText(_translate("c", "File Name:"))
        self.downloadSaveButton.setText(_translate("c", "Save"))
        self.InterGroupBox.setTitle(_translate("c", "Interaction"))
        self.interLabel.setText(_translate("c", "Interaction Name:"))
        self.interSaveButton.setText(_translate("c", "Save"))


if __name__ == "__main__":
    import sys
    import os

    app = QtWidgets.QApplication(sys.argv)
    c = QtWidgets.QMainWindow()
    ui = VRGAutomation()
    userName = os.getlogin()
    ui.setupUi(c)
    c.show()
    sys.exit(app.exec_())
