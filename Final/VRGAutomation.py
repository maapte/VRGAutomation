import json

from PyQt5 import QtCore, QtGui, QtWidgets

from Download import Download
from Form import Form
from GenerateVRG import GenerateVrg
from InteractionPage import InteractionPage
from StandalonePage import StandalonePage
from Steps import Steps
from Vrg import Vrg
from constant.ApplicationConstant import *
import sys
import os


# noinspection PyArgumentList
class VRGAutomation(object):
    def __init__(self):
        self.central_widget = ""
        self.application_title = None
        self.project_name_label = None
        self.project_name = None
        self.user_name_label = None
        self.user_name = None
        self.brand_label = None
        self.brand_combo_box = None
        self.application_type_label = None
        self.application_type_combo = None
        self.site_type_combo = None
        self.site_type_label = None
        self.site_name_label = None
        self.site_name = None

        self.add_button = None
        self.add_flow = None
        self.download_button = None
        self.interaction_button = None

        self.standalone_page_box = None
        self.page_name_standalone = None
        self.page_name_standalone_label = None
        self.page_hierarchy_standalone = None
        self.page_hierarchy_standalone_label = None
        self.error_group_box_standalone = None
        self.yes_error_standalone = None
        self.no_error_standalone = None
        self.login_group_box_page = None
        self.yes_login_standalone = None
        self.no_login_standalone = None
        self.both_login_standalone = None
        self.save_button_standalone = None
        self.cancel_button_standalone = None

        self.form_group_box = None
        self.form_name_label_form_box = None
        self.form_name_form_box = None
        self.no_of_steps_label_form_box = None
        self.no_of_steps_form_box = None
        self.product_checkbox_form_box = None
        self.transaction_checkbox_form_box = None
        self.generate_steps_form_box = None

        self.step_group_box = None
        self.page_name_label_steps = None
        self.page_name_steps = None
        self.step_name_label_steps = None
        self.step_name_steps = None
        self.page_hierarchy_label_steps = None
        self.page_hierarchy_steps = None
        self.login_group_box_steps = None
        self.yes_login_group_box_steps = None
        self.no_login_group_box_steps = None
        self.both_login_group_box_steps = None
        self.form_group_box_steps = None
        self.form_view_steps = None
        self.form_submit_steps = None
        self.form_qualify_steps = None
        self.form_steps = None
        self.error_group_box_steps = None
        self.yes_error_group_box_steps = None
        self.no_error_group_box_steps = None
        self.error_form_group_box_steps = None
        self.yes_error_form_group_box_steps = None
        self.no_error_form_group_box_steps = None
        self.product_group_box_steps = None
        self.product_app_group_box_steps = None
        self.personal_details_steps = None
        self.summary_steps = None
        self.confirmation_steps = None
        self.product_recommendation_steps = None
        self.terms_and_condition_steps = None
        self.is_paperless_steps = None
        self.product_id_label_steps = None
        self.product_id_steps = None
        self.parent_product_label_steps = None
        self.parent_product_steps = None
        self.adjudication_label_steps = None
        self.adjudication_steps = None
        self.positioning_label_steps = None
        self.positioning_combo_box_steps = None
        self.grouping_label_steps = None
        self.grouping_combo_box = None
        self.fulfillment_label_steps = None
        self.fulfillment_combo_box_steps = None
        self.transaction_group_box_steps = None
        self.from_label_steps = None
        self.from_text_steps = None
        self.to_label_steps = None
        self.to_text_steps = None
        self.is_external_check_box_steps = None
        self.error_steps_group_box = None
        self.yes_error_steps_group_box = None
        self.no_error_steps_group_box = None
        self.save_and_next_steps = None
        self.cancel_steps = None

        self.download_group_box = None
        self.download_label = None
        self.download_name = None
        self.download_type_label = None
        self.download_type_combo_box = None
        self.download_save_button = None

        self.interaction_group_box = None
        self.interaction_label = None
        self.interaction_name = None
        self.interaction_save_button = None

        self.list_group_box = None
        self.list_combo_box = None
        self.list_edit_button = None
        self.list_delete_button = None

        self.generate_vrg_button = None
        self.close_vrg_button = None
        self.reset_button = None

        self.menu_bar = None
        self.status_bar = None

        self.vrg = Vrg()
        self.formObj = Form()
        self.counter = 0
        self.order = list()
        self.editFlag = 0
        self.steps = list()

    @staticmethod
    def close_button(self):
        sys.exit(app.exec_())

    def reset(self):
        self.clear_steps_fields()
        self.clear_form_values()
        self.vrg.forms.clear()
        self.vrg.pages.clear()
        self.vrg.download.clear()
        self.vrg.interaction.clear()
        self.project_name.setEnabled(LABEL_TRUE)
        self.site_name.setEnabled(LABEL_TRUE)
        self.site_type_combo.setEnabled(LABEL_TRUE)
        self.brand_combo_box.setEnabled(LABEL_TRUE)
        self.application_type_combo.setEnabled(LABEL_TRUE)
        self.project_name.setText("")
        self.site_name.setText("")
        self.brand_combo_box.setCurrentText("")
        self.application_type_combo.setCurrentText("")
        self.site_type_combo.setCurrentText("")
        self.standalone_page_box.setEnabled(LABEL_FALSE)
        self.form_group_box.setEnabled(LABEL_FALSE)
        self.step_group_box.setEnabled(LABEL_FALSE)
        self.download_group_box.setEnabled(LABEL_FALSE)
        self.interaction_group_box.setEnabled(LABEL_FALSE)
        self.list_combo_box.clear()

    def cancel_standalone_page(self):
        self.standalone_page_box.setEnabled(LABEL_FALSE)

    def cancel_step_page(self):
        self.clear_steps_fields()
        self.step_group_box.setEnabled(LABEL_FALSE)

    def save_form_page(self):
        self.formObj.formName = self.form_name_form_box.text().lower()
        self.formObj.noOfSteps = self.no_of_steps_form_box.text()
        self.form_group_box.setEnabled(LABEL_FALSE)
        self.step_group_box.setEnabled(LABEL_TRUE)
        self.form_steps.setChecked(LABEL_TRUE)
        self.form_steps.setEnabled(LABEL_FALSE)
        if self.product_checkbox_form_box.isChecked():
            self.product_group_box_steps.setEnabled(LABEL_TRUE)
            self.formObj.isProductExist = str(
                self.product_checkbox_form_box.isChecked()
            )
            self.formObj.set_is_product_exist("true")
        else:
            self.product_group_box_steps.setEnabled(False)
        if self.transaction_checkbox_form_box.isChecked():
            self.transaction_group_box_steps.setEnabled(LABEL_TRUE)
            self.formObj.isTransactionExist = str(
                self.transaction_checkbox_form_box.isChecked()
            )
            self.formObj.set_is_transaction_exist("true")
        else:
            self.transaction_group_box_steps.setEnabled(LABEL_FALSE)

    def step_page_details(self):
        steps_obj = Steps()
        steps_obj.set_step_name(self.step_name_steps.text())
        if self.application_type_combo.currentText() == APPLICATION_EMBER:
            steps_obj.set_page_name(
                str(self.page_hierarchy_steps.text().lower().replace(" ", "-"))
            )
            steps_obj.set_page_hierarchy(
                str(self.page_hierarchy_steps.text().lower().replace(" ", "-"))
            )
        if (
            self.application_type_combo.currentText() == APPLICATION_ANGULAR
            or self.application_type_combo.currentText() == APPLICATION_MOBILE_JSON
        ):
            steps_obj.set_page_name(
                str(self.page_name_steps.text().lower().replace(" ", "-"))
            )
            steps_obj.set_page_hierarchy(
                str(self.page_hierarchy_steps.text().lower().replace(" ", "-"))
            )

        steps_obj.set_from_transaction(self.from_text_steps.text())
        steps_obj.set_to_transaction(self.to_text_steps.text())
        steps_obj.set_is_external(str(self.is_external_check_box_steps.isChecked()))

        steps_obj.set_form_view(str(self.form_view_steps.isChecked()))
        steps_obj.set_form_qualify(str(self.form_qualify_steps.isChecked()))
        steps_obj.set_form_submit(str(self.form_submit_steps.isChecked()))

        steps_obj.set_product_id(self.product_id_steps.text())
        steps_obj.set_parent_product(self.parent_product_steps.text())
        steps_obj.set_adjudication(self.adjudication_steps.text())
        steps_obj.set_product_positioning(
            self.positioning_combo_box_steps.currentText()
        )
        steps_obj.set_product_grouping(self.grouping_combo_box.currentText())
        steps_obj.set_fulfillment(self.fulfillment_combo_box_steps.currentText())

        steps_obj.set_personal_details(str(self.personal_details_steps.isChecked()))
        steps_obj.set_summary(str(self.summary_steps.isChecked()))
        steps_obj.set_product_recommendation(
            str(self.product_recommendation_steps.isChecked())
        )
        steps_obj.set_terms_and_condition(
            str(self.terms_and_condition_steps.isChecked())
        )
        steps_obj.set_confirmation(str(self.confirmation_steps.isChecked()))
        steps_obj.set_is_paperless(str(self.is_paperless_steps.isChecked()))

        if self.yes_login_group_box_steps.isChecked():
            steps_obj.set_user_id("{dynamic}")
            steps_obj.set_user_auth_state("{dynamic}")
            steps_obj.set_user_type("{dynamic}")
            steps_obj.set_both_step("false")

        elif self.both_login_group_box_steps.isChecked():
            steps_obj.set_user_id("{dynamic}")
            steps_obj.set_user_auth_state("{dynamic}")
            steps_obj.set_user_type("{dynamic}")
            steps_obj.set_both_step("true")

        elif self.no_login_group_box_steps.isChecked():
            steps_obj.set_both_step("false")

        if self.yes_error_steps_group_box.isChecked():
            steps_obj.eventError = "true"
            steps_obj.errorMessage = "{dynamic}"
            steps_obj.errorsCode = "{dynamic}"
            steps_obj.errorsSubType = "{dynamic}"
            steps_obj.errorsType = "{dynamic}"
            steps_obj.errorsField = "{dynamic}"

        return steps_obj

    def save_steps_information(self):
        no_of_steps = int(self.no_of_steps_form_box.text())
        steps_obj = Steps()
        if len(self.steps) == 0:
            steps_obj = self.step_page_details()

        elif len(self.steps) < no_of_steps:
            steps_obj = self.step_page_details()

        elif len(self.steps) == no_of_steps:
            steps_obj = self.step_page_details()
            if self.product_checkbox_form_box.isChecked():
                self.formObj.set_is_product_exist("true")
            else:
                self.formObj.set_is_product_exist("false")

            if self.transaction_checkbox_form_box.isChecked():
                self.formObj.set_is_transaction_exist("true")
            else:
                self.formObj.set_is_transaction_exist("false")

        if self.editFlag == 1:
            edit_name = self.list_combo_box.currentText()
            steps_obj = self.step_page_details()
            for i in range(0, len(self.vrg.forms)):
                for j in range(0, len(self.vrg.forms[i]["steps"])):
                    if "step_name" in self.vrg.forms[i]["steps"][j]:
                        f1 = self.vrg.forms[i]["form_name"] + "-"
                        step_name_edit = str(edit_name).replace(str(f1), "")
                        if (
                            self.vrg.forms[i]["steps"][j]["step_name"]
                            == step_name_edit
                        ):
                            step = json.dumps(steps_obj.__dict__)
                            self.vrg.forms[i]["steps"][j] = json.loads(step)
                            self.clear_steps_fields()
                            self.step_group_box.setEnabled(LABEL_FALSE)
                            self.clear_form_values()
                            self.form_group_box.setEnabled(LABEL_FALSE)
                            self.add_flow.setEnabled(LABEL_TRUE)
                            self.add_button.setEnabled(LABEL_TRUE)
                            self.interaction_button.setEnabled(LABEL_TRUE)
                            self.download_button.setEnabled(LABEL_TRUE)

        self.vrg.set_project_name(self.project_name.text().lower().replace(" ", "-"))
        self.vrg.set_user_name(self.user_name.text().lower())
        self.vrg.set_site_name(self.site_name.text().lower().replace(" ", "-"))
        self.vrg.set_site_brand(
            self.brand_combo_box.currentText().lower().replace(" ", "-")
        )
        self.vrg.set_application_types(
            self.application_type_combo.currentText().lower().replace(" ", "-")
        )
        self.vrg.set_site_type(
            self.site_type_combo.currentText().lower().replace(" ", "-")
        )

        if len(self.steps) >= 0 and self.editFlag == 0:
            step = json.dumps(steps_obj.__dict__)
            self.steps.append(json.loads(step))
            self.clear_steps_fields()
        if len(self.steps) == no_of_steps and self.editFlag == 0:

            if self.product_checkbox_form_box.isChecked():
                self.product_group_box_steps.setEnabled(LABEL_TRUE)
                self.formObj.isProductExist = str(
                    self.product_checkbox_form_box.isChecked()
                )
                self.formObj.set_is_product_exist("true")
            else:
                self.product_group_box_steps.setEnabled(False)
                self.formObj.set_is_product_exist("false")
            if self.transaction_checkbox_form_box.isChecked():
                self.transaction_group_box_steps.setEnabled(True)
                self.formObj.isTransactionExist = str(
                    self.transaction_checkbox_form_box.isChecked()
                )
                self.formObj.set_is_transaction_exist("true")
            else:
                self.transaction_group_box_steps.setEnabled(LABEL_FALSE)
                self.formObj.set_is_transaction_exist("false")

            form_obj = {
                "form_name": self.form_name_form_box.text().lower(),
                "no_of_steps": self.no_of_steps_form_box.text(),
                "is_product_exist": self.formObj.get_is_product_exist,
                "is_transaction_exist": self.formObj.get_is_transaction_exist,
                "steps": self.steps,
            }
            form_obj_dump = json.dumps(form_obj)
            self.vrg.forms.append(json.loads(form_obj_dump))
            self.step_group_box.setEnabled(LABEL_FALSE)
            self.add_flow.setEnabled(LABEL_TRUE)
            self.add_button.setEnabled(LABEL_TRUE)
            self.interaction_button.setEnabled(LABEL_TRUE)
            self.download_button.setEnabled(LABEL_TRUE)
        self.editFlag = 0
        self.list_combo_box.clear()
        for i in range(0, len(self.vrg.pages)):
            if self.application_type_combo.currentText() != "Ember":
                if "page_name" in self.vrg.pages[i]:
                    v1 = self.vrg.pages[i]["page_name"]
                    self.list_combo_box.addItem(v1)
            else:
                if "page_hierarchy" in self.vrg.pages[i]:
                    v1 = self.vrg.pages[i]["page_hierarchy"]
                    self.list_combo_box.addItem(v1)

        for i in range(0, len(self.vrg.forms)):
            for j in range(0, len(self.vrg.forms[i]["steps"])):
                if "step_name" in self.vrg.forms[i]["steps"][j]:
                    f1 = (
                        self.vrg.forms[i]["form_name"]
                        + "-"
                        + self.vrg.forms[i]["steps"][j]["step_name"]
                    )
                    self.list_combo_box.addItem(f1)

    def clear_form_values(self):
        self.form_name_form_box.setText("")
        self.no_of_steps_form_box.setText("")
        self.transaction_checkbox_form_box.setChecked(LABEL_FALSE)
        self.product_checkbox_form_box.setChecked(LABEL_FALSE)

    def clear_steps_fields(self):
        self.step_name_steps.setText("")
        self.page_name_steps.setText("")
        self.page_hierarchy_steps.setText("")
        self.from_text_steps.setText("")
        self.to_text_steps.setText("")
        self.form_view_steps.setChecked(LABEL_FALSE)
        self.form_submit_steps.setChecked(LABEL_FALSE)
        self.form_qualify_steps.setChecked(LABEL_FALSE)
        self.is_external_check_box_steps.setChecked(LABEL_FALSE)
        self.product_id_steps.setText("")
        self.parent_product_steps.setText("")
        self.adjudication_steps.setText("")
        self.positioning_combo_box_steps.setCurrentText("Not Applicable")
        self.grouping_combo_box.setCurrentText("Not Applicable")
        self.fulfillment_combo_box_steps.setCurrentText("Not Applicable")
        self.yes_login_group_box_steps.setChecked(LABEL_FALSE)
        self.both_login_group_box_steps.setChecked(LABEL_FALSE)
        self.no_login_group_box_steps.setChecked(LABEL_FALSE)
        self.personal_details_steps.setChecked(LABEL_FALSE)
        self.summary_steps.setChecked(LABEL_FALSE)
        self.confirmation_steps.setChecked(LABEL_FALSE)
        self.product_recommendation_steps.setChecked(LABEL_FALSE)
        self.terms_and_condition_steps.setChecked(LABEL_FALSE)
        self.is_paperless_steps.setChecked(LABEL_FALSE)

    def generate_button(self):
        self.vrg.set_project_name(self.project_name.text().lower().replace(" ", "-"))
        self.vrg.set_user_name(self.user_name.text().lower())
        self.vrg.set_site_name(self.site_name.text().lower().replace(" ", "-"))
        self.vrg.set_site_brand(
            self.brand_combo_box.currentText().lower().replace(" ", "-")
        )
        self.vrg.set_application_types(
            self.application_type_combo.currentText().lower().replace(" ", "-")
        )
        self.vrg.set_site_type(
            self.site_type_combo.currentText().lower().replace(" ", "-")
        )
        obj = self.vrg
        json_page = json.dumps(obj.__dict__)
        application_object = GenerateVrg()
        val = json.loads(json_page)
        print("GENERATE: ", val)
        application_object.generate_VRG(val)

    def add_flow_page(self):
        self.standalone_page_box.setEnabled(LABEL_FALSE)
        self.form_group_box.setEnabled(LABEL_TRUE)
        self.step_group_box.setEnabled(LABEL_FALSE)
        self.add_button.setEnabled(LABEL_FALSE)
        self.add_flow.setEnabled(LABEL_FALSE)
        self.download_button.setEnabled(LABEL_FALSE)
        self.interaction_button.setEnabled(LABEL_FALSE)
        self.disable_project_info()
        self.clear_form_values()
        self.clear_steps_fields()
        self.steps.clear()

    def application_type(self):
        if self.application_type_combo.currentText() == APPLICATION_EMBER:
            self.page_name_standalone_label.setText("Page Name :")
            self.page_hierarchy_standalone_label.setText("Route Name:")
            self.page_name_label_steps.setText("Page Name")
            self.page_hierarchy_label_steps.setText("Route Name")
            self.page_name_standalone.setEnabled(LABEL_FALSE)
            self.page_name_steps.setEnabled(LABEL_FALSE)
        if self.application_type_combo.currentText() == APPLICATION_ANGULAR:
            self.page_name_standalone_label.setText("Page Name :")
            self.page_hierarchy_standalone_label.setText("Page Hierarchy : ")
            self.page_name_label_steps.setText("Page Name : ")
            self.page_hierarchy_label_steps.setText("Page Hierarchy : ")
            self.page_name_standalone.setEnabled(LABEL_TRUE)
            self.page_name_steps.setEnabled(LABEL_TRUE)
        if self.application_type_combo.currentText() == APPLICATION_MOBILE_JSON:
            self.page_name_standalone_label.setText("Page Name :")
            self.page_hierarchy_standalone_label.setText("Page Hierarchy : ")
            self.page_name_label_steps.setText("Page Name : ")
            self.page_hierarchy_label_steps.setText("Page Hierarchy : ")

    def site_type(self):
        if self.site_type_combo.currentText() == "Desktop":
            self.vrg.set_site_type("desktop")
        if self.site_type_combo.currentText() == "Mobile":
            self.vrg.set_site_type("mobile")
        if self.site_type_combo.currentText() == "Responsive":
            self.vrg.set_site_type("responsive")

    def disable_project_info(self):
        self.project_name.setEnabled(LABEL_FALSE)
        self.brand_combo_box.setEnabled(LABEL_FALSE)
        self.application_type_combo.setEnabled(LABEL_FALSE)
        self.site_type_combo.setEnabled(LABEL_FALSE)
        self.site_name.setEnabled(LABEL_FALSE)

    def add_page_button(self):
        self.standalone_page_box.setEnabled(LABEL_TRUE)
        self.form_group_box.setEnabled(LABEL_FALSE)
        self.step_group_box.setEnabled(LABEL_FALSE)
        self.add_button.setEnabled(LABEL_FALSE)
        self.add_flow.setEnabled(LABEL_FALSE)
        self.download_button.setEnabled(LABEL_FALSE)
        self.interaction_button.setEnabled(LABEL_FALSE)
        self.interaction_group_box.setEnabled(LABEL_FALSE)
        self.download_group_box.setEnabled(LABEL_FALSE)
        self.disable_project_info()

    def interaction_button_page(self):
        self.interaction_group_box.setEnabled(LABEL_TRUE)
        self.standalone_page_box.setEnabled(LABEL_FALSE)
        self.form_group_box.setEnabled(LABEL_FALSE)
        self.step_group_box.setEnabled(LABEL_FALSE)
        self.add_button.setEnabled(LABEL_FALSE)
        self.add_flow.setEnabled(LABEL_FALSE)
        self.interaction_button.setEnabled(LABEL_FALSE)
        self.download_button.setEnabled(LABEL_FALSE)
        self.disable_project_info()

    def download_button_page(self):
        self.download_group_box.setEnabled(LABEL_TRUE)
        self.standalone_page_box.setEnabled(LABEL_FALSE)
        self.form_group_box.setEnabled(LABEL_FALSE)
        self.step_group_box.setEnabled(LABEL_FALSE)
        self.add_button.setEnabled(LABEL_FALSE)
        self.add_flow.setEnabled(LABEL_FALSE)
        self.interaction_button.setEnabled(LABEL_FALSE)
        self.download_button.setEnabled(LABEL_FALSE)
        self.interaction_group_box.setEnabled(LABEL_FALSE)
        self.disable_project_info()

    def save_download_information(self):
        download_obj = Download()
        download_obj.download_file_name = str(
            self.download_name.text().lower().replace(" ", "-")
        )
        download_obj.download_file_type = str(
            self.download_type_combo_box.currentText().lower().replace(" ", "-")
        )
        download_section = json.dumps(download_obj.__dict__)

        self.vrg.download.append(json.loads(download_section))
        self.download_name.setText("")
        self.download_type_combo_box.setCurrentIndex(0)

        self.download_group_box.setEnabled(LABEL_FALSE)
        self.add_button.setEnabled(LABEL_TRUE)
        self.interaction_button.setEnabled(LABEL_TRUE)
        self.download_button.setEnabled(LABEL_TRUE)
        self.add_flow.setEnabled(LABEL_TRUE)

    def save_interaction_information(self):
        interaction = InteractionPage()
        interaction.siteInteractionEvent = "true"
        interaction.interactionName = self.interaction_name.text()
        interaction_action = json.dumps(interaction.__dict__)
        self.vrg.interaction.append(json.loads(interaction_action))
        self.interaction_name.setText("")
        self.interaction_group_box.setEnabled(LABEL_FALSE)
        self.add_button.setEnabled(LABEL_TRUE)
        self.interaction_button.setEnabled(LABEL_TRUE)
        self.download_button.setEnabled(LABEL_TRUE)
        self.add_flow.setEnabled(LABEL_TRUE)

    def save_standalone_page(self):
        edit_name = self.list_combo_box.currentText()
        obj1 = StandalonePage()
        if self.application_type_combo.currentText() == APPLICATION_EMBER:
            obj1.set_page_name(
                str(self.page_name_standalone.text().lower().replace(" ", "-"))
            )
            obj1.set_route_name(
                str(self.page_hierarchy_standalone.text().lower().replace(" ", "-"))
            )
            obj1.set_page_hierarchy(
                str(self.page_hierarchy_standalone.text().lower().replace(" ", "-"))
            )
            obj1.set_page_path(
                str(self.page_name_standalone.text().lower().replace(" ", "-"))
            )
        if (
            self.application_type_combo.currentText() == APPLICATION_ANGULAR
            or self.application_type_combo.currentText() == APPLICATION_MOBILE_JSON
        ):
            obj1.set_page_name(
                str(self.page_name_standalone.text().lower().replace(" ", "-"))
            )
            obj1.set_page_hierarchy(
                str(self.page_hierarchy_standalone.text().lower().replace(" ", "-"))
            )
            obj1.set_page_path(
                str(self.page_name_standalone.text().lower().replace(" ", "-"))
            )

        # Error Code Checked or Unchecked
        if self.yes_error_standalone.isChecked():
            obj1.eventError = "true"
            obj1.errorMessage = "{dynamic}"
            obj1.errorsCode = "{dynamic}"
            obj1.errorsType = "{dynamic}"
            obj1.errorsSubType = "{dynamic}"
            obj1.errorsField = "{dynamic}"
            obj1.set_event_error("true")

        # Login Code Checked or Unchecked
        if self.yes_login_standalone.isChecked():
            obj1.set_user_id("{dynamic}")
            obj1.set_user_auth_state("authenticated")
            obj1.set_user_type("{dynamic}")
            obj1.set_login_event("true")
            obj1.set_both("false")
        elif self.no_login_standalone.isChecked():
            obj1.set_user_id("")
            obj1.set_user_auth_state("non-authenticated")
            obj1.set_user_type("")
            obj1.set_event_error("false")
            obj1.set_both("false")
        elif self.both_login_standalone.isChecked():
            obj1.set_user_id("{dynamic}")
            obj1.set_user_auth_state("authenticated")
            obj1.set_user_type("{dynamic}")
            obj1.set_login_event("true")
            obj1.set_both("true")

        if self.editFlag == 1:
            for i in range(0, len(self.vrg.pages)):
                if "page_name" in self.vrg.pages[i]:
                    if self.vrg.pages[i]["page_name"] == edit_name:
                        page = json.dumps(obj1.__dict__)
                        v = json.loads(page)
                        self.vrg.pages[i] = v
                if "page_hierarchy" in self.vrg.pages[i]:
                    if self.vrg.pages[i]["page_hierarchy"] == edit_name:
                        page = json.dumps(obj1.__dict__)
                        v = json.loads(page)
                        self.vrg.pages[i] = v

        if len(self.vrg.pages) >= 0 and self.editFlag == 0:
            page = json.dumps(obj1.__dict__)
            self.vrg.pages.append(json.loads(page))

        self.page_name_standalone.setText("")
        self.page_hierarchy_standalone.setText("")
        self.from_text_steps.setText("")
        self.to_text_steps.setText("")
        self.yes_error_standalone.setChecked(LABEL_FALSE)
        self.no_error_standalone.setChecked(LABEL_FALSE)
        self.yes_login_standalone.setChecked(LABEL_FALSE)
        self.no_login_standalone.setChecked(LABEL_FALSE)
        self.standalone_page_box.setEnabled(LABEL_FALSE)
        self.add_button.setEnabled(LABEL_TRUE)
        self.add_flow.setEnabled(LABEL_TRUE)
        self.download_button.setEnabled(LABEL_TRUE)
        self.interaction_button.setEnabled(LABEL_TRUE)
        self.editFlag = 0
        self.list_combo_box.clear()
        for i in range(0, len(self.vrg.pages)):
            if self.application_type_combo.currentText() != APPLICATION_EMBER:
                if "page_name" in self.vrg.pages[i]:
                    v1 = self.vrg.pages[i]["page_name"]
                    self.list_combo_box.addItem(v1)
            else:
                if "page_hierarchy" in self.vrg.pages[i]:
                    v1 = self.vrg.pages[i]["page_hierarchy"]
                    self.list_combo_box.addItem(v1)

        for i in range(0, len(self.vrg.forms)):
            if self.application_type_combo.currentText() != APPLICATION_EMBER:
                for j in range(0, len(self.vrg.forms[i]["steps"])):
                    if "step_name" in self.vrg.forms[i]["steps"][j]:
                        f1 = (
                            self.vrg.forms[i]["form_name"]
                            + "-"
                            + self.vrg.forms[i]["steps"][j]["step_name"]
                        )
                        self.list_combo_box.addItem(f1)
            else:
                for j in range(0, len(self.vrg.forms[i]["steps"])):
                    if "page_hierarchy" in self.vrg.forms[i]["steps"][j]:
                        f1 = (
                            self.vrg.forms[i]["form_name"]
                            + "-"
                            + self.vrg.forms[i]["steps"][j]["page_hierarchy"]
                        )
                        self.list_combo_box.addItem(f1)

    def edit_list_box_button(self):
        name = self.list_combo_box.currentText()
        standalone_page_detail = StandalonePage()
        self.editFlag = 1
        self.steps_edit = 0
        flag = ""
        for i in range(0, len(self.vrg.pages)):
            if self.application_type_combo.currentText() != APPLICATION_EMBER:
                if "page_name" in self.vrg.pages[i]:
                    if self.vrg.pages[i]["page_name"] == name:
                        flag = "PAGES"
                        break
            else:
                if "page_hierarchy" in self.vrg.pages[i]:
                    if self.vrg.pages[i]["page_hierarchy"] == name:
                        flag = "PAGES"
                        break

        if flag != "PAGES" or flag == "":
            for i in range(0, len(self.vrg.forms)):
                for j in range(0, len(self.vrg.forms[i]["steps"])):
                    if "step_name" in self.vrg.forms[i]["steps"][j] and flag != "STEPS":
                        f1 = self.vrg.forms[i]["form_name"] + "-"
                        step_name_edit = str(name).replace(str(f1), "")
                        if (
                            self.vrg.forms[i]["steps"][j]["step_name"]
                            == step_name_edit
                        ):
                            flag = "STEPS"
                            break

        if flag == "PAGES":
            for i in range(0, len(self.vrg.pages)):
                if (
                    "page_name" in self.vrg.pages[i]
                    or "page_hierarchy" in self.vrg.pages[i]
                ):
                    if (
                        self.vrg.pages[i]["page_name"] == name
                        or self.vrg.pages[i]["page_hierarchy"] == name
                    ):
                        self.standalone_page_box.setEnabled(LABEL_TRUE)
                        standalone_page_detail.set_page_name(
                            self.vrg.pages[i]["page_name"]
                        )
                        standalone_page_detail.set_route_name(
                            self.vrg.pages[i]["page_hierarchy"]
                        )
                        standalone_page_detail.set_page_referrer(
                            self.vrg.pages[i]["page_referrer"]
                        )
                        standalone_page_detail.set_page_path(
                            self.vrg.pages[i]["page_path"]
                        )
                        standalone_page_detail.set_page_hierarchy(
                            self.vrg.pages[i]["page_hierarchy"]
                        )
                        standalone_page_detail.set_both(self.vrg.pages[i]["both"])
                        if len(self.vrg.pages[i]["user_id"]) == 0:
                            standalone_page_detail.set_user_id("false")
                        else:
                            standalone_page_detail.set_user_id("true")
                        if self.vrg.pages[i]["event_error"] == "false":
                            standalone_page_detail.set_error_code("false")
                        if self.vrg.pages[i]["event_error"] == "true":
                            standalone_page_detail.set_error_code("true")
                        self.page_name_standalone.setText(
                            standalone_page_detail.get_page_name
                        )
                        self.page_hierarchy_standalone.setText(
                            standalone_page_detail.get_page_hierarchy
                        )
                        if (
                            standalone_page_detail.get_user_id == "true"
                            and standalone_page_detail.get_both == "false"
                        ):
                            self.yes_login_standalone.setChecked(LABEL_TRUE)
                            self.no_login_standalone.setChecked(LABEL_FALSE)
                            self.both_login_standalone.setChecked(LABEL_FALSE)
                        elif (
                            standalone_page_detail.get_user_id == "true"
                            and standalone_page_detail.get_both == "true"
                        ):
                            self.both_login_standalone.setChecked(LABEL_TRUE)
                            self.yes_login_standalone.setChecked(LABEL_FALSE)
                            self.no_login_standalone.setChecked(LABEL_FALSE)
                        else:
                            self.both_login_standalone.setChecked(LABEL_FALSE)
                            self.yes_login_standalone.setChecked(LABEL_FALSE)
                            self.no_login_standalone.setChecked(LABEL_TRUE)

                        if standalone_page_detail.get_error_code == "true":
                            self.yes_error_standalone.setChecked(LABEL_TRUE)
                            self.no_error_standalone.setChecked(LABEL_FALSE)
                        else:
                            self.yes_error_standalone.setChecked(LABEL_FALSE)
                            self.no_error_standalone.setChecked(LABEL_TRUE)

        if flag == "STEPS":
            for i in range(0, len(self.vrg.forms)):
                for j in range(0, len(self.vrg.forms[i]["steps"])):
                    if "step_name" in self.vrg.forms[i]["steps"][j] and self.steps_edit == 0:
                        f1 = self.vrg.forms[i]["form_name"] + "-"
                        step_name_edit = str(name).replace(str(f1), "")
                        if (
                            self.vrg.forms[i]["steps"][j]["step_name"]
                            == step_name_edit
                        ):
                            self.steps_edit = 1
                            self.form_name_form_box.setText(
                                str(self.vrg.forms[i]["form_name"])
                            )
                            self.no_of_steps_form_box.setText(
                                str(self.vrg.forms[i]["no_of_steps"])
                            )
                            if self.vrg.forms[i]["is_product_exist"] == "true":
                                self.product_checkbox_form_box.setChecked(LABEL_TRUE)
                                self.product_group_box_steps.setEnabled(LABEL_TRUE)
                            else:
                                self.product_checkbox_form_box.setChecked(LABEL_FALSE)
                                self.product_group_box_steps.setEnabled(LABEL_FALSE)
                            if self.vrg.forms[i]["is_transaction_exist"] == "true":
                                self.transaction_checkbox_form_box.setChecked(True)
                                self.transaction_group_box_steps.setEnabled(LABEL_TRUE)
                            else:
                                self.transaction_checkbox_form_box.setChecked(
                                    LABEL_FALSE
                                )
                                self.transaction_group_box_steps.setEnabled(LABEL_FALSE)

                            self.step_group_box.setEnabled(LABEL_TRUE)
                            steps_obj = Steps()
                            steps_obj.set_step_name(
                                self.vrg.forms[i]["steps"][j]["step_name"]
                            )
                            steps_obj.set_page_name(
                                self.vrg.forms[i]["steps"][j]["page_name"]
                            )
                            steps_obj.set_page_hierarchy(
                                self.vrg.forms[i]["steps"][j]["page_hierarchy"]
                            )
                            steps_obj.set_user_id(
                                self.vrg.forms[i]["steps"][j]["user_id"]
                            )
                            steps_obj.set_user_type(
                                self.vrg.forms[i]["steps"][j]["user_type"]
                            )
                            steps_obj.set_user_auth_state(
                                self.vrg.forms[i]["steps"][j]["user_auth_state"]
                            )
                            steps_obj.set_from_transaction(
                                self.vrg.forms[i]["steps"][j]["from_transaction"]
                            )
                            steps_obj.set_to_transaction(
                                self.vrg.forms[i]["steps"][j]["to_transaction"]
                            )
                            steps_obj.set_is_external(
                                self.vrg.forms[i]["steps"][j]["is_external"]
                            )
                            steps_obj.set_form_view(
                                self.vrg.forms[i]["steps"][j]["form_view"]
                            )
                            steps_obj.set_form_qualify(
                                self.vrg.forms[i]["steps"][j]["form_qualify"]
                            )
                            steps_obj.set_form_submit(
                                self.vrg.forms[i]["steps"][j]["form_submit"]
                            )
                            steps_obj.set_product_id(
                                self.vrg.forms[i]["steps"][j]["product_id"]
                            )
                            steps_obj.set_parent_product(
                                self.vrg.forms[i]["steps"][j]["parent_product"]
                            )
                            steps_obj.set_adjudication(
                                self.vrg.forms[i]["steps"][j]["adjudication"]
                            )
                            steps_obj.set_product_positioning(
                                self.vrg.forms[i]["steps"][j]["product_positioning"]
                            )
                            steps_obj.set_product_grouping(
                                self.vrg.forms[i]["steps"][j]["product_grouping"]
                            )
                            steps_obj.set_fulfillment(
                                self.vrg.forms[i]["steps"][j]["fulfillment"]
                            )
                            steps_obj.set_event_error(
                                self.vrg.forms[i]["steps"][j]["event_error"]
                            )
                            steps_obj.set_personal_details(
                                self.vrg.forms[i]["steps"][j]["personal_details"]
                            )
                            steps_obj.set_summary(
                                self.vrg.forms[i]["steps"][j]["summary"]
                            )
                            steps_obj.set_product_recommendation(
                                self.vrg.forms[i]["steps"][j]["product_recommendation"]
                            )
                            steps_obj.set_terms_and_condition(
                                self.vrg.forms[i]["steps"][j]["terms_and_condition"]
                            )
                            steps_obj.set_confirmation(
                                self.vrg.forms[i]["steps"][j]["confirmation"]
                            )
                            steps_obj.set_is_paperless(
                                self.vrg.forms[i]["steps"][j]["is_paperless"]
                            )
                            steps_obj.set_both_step(
                                self.vrg.forms[i]["steps"][j]["both_step"]
                            )
                            self.step_group_box.setEnabled(LABEL_TRUE)
                            self.step_name_steps.setText(steps_obj.get_step_name)
                            self.page_name_steps.setText(steps_obj.get_page_name)
                            self.page_hierarchy_steps.setText(
                                steps_obj.get_page_hierarchy
                            )
                            self.from_text_steps.setText(steps_obj.get_from_transaction)
                            self.to_text_steps.setText(steps_obj.get_to_transaction)
                            if steps_obj.get_is_external == "True":
                                self.is_external_check_box_steps.setChecked(LABEL_TRUE)
                            else:
                                self.is_external_check_box_steps.setChecked(LABEL_FALSE)
                            if steps_obj.get_form_view == "True":
                                self.form_view_steps.setChecked(LABEL_TRUE)
                            else:
                                self.form_view_steps.setChecked(LABEL_FALSE)

                            if steps_obj.get_form_qualify == "True":
                                self.form_qualify_steps.setChecked(LABEL_TRUE)
                            else:
                                self.form_qualify_steps.setChecked(LABEL_FALSE)

                            if steps_obj.get_form_submit == "True":
                                self.form_submit_steps.setChecked(LABEL_TRUE)
                            else:
                                self.form_submit_steps.setChecked(LABEL_FALSE)

                                self.form_steps.setChecked(LABEL_TRUE)

                            self.product_id_steps.setText(steps_obj.get_product_id)
                            self.parent_product_steps.setText(
                                steps_obj.get_parent_product
                            )
                            self.adjudication_steps.setText(steps_obj.get_adjudication)
                            self.positioning_combo_box_steps.setCurrentText(
                                steps_obj.get_product_positioning
                            )
                            self.grouping_combo_box.setCurrentText(
                                steps_obj.get_product_grouping
                            )
                            self.fulfillment_combo_box_steps.setCurrentText(
                                steps_obj.get_fulfillment
                            )

                            if steps_obj.get_personal_details == "True":
                                self.personal_details_steps.setChecked(LABEL_TRUE)
                            else:
                                self.personal_details_steps.setChecked(LABEL_FALSE)

                            if steps_obj.get_summary == "True":
                                self.summary_steps.setChecked(LABEL_TRUE)
                            else:
                                self.summary_steps.setChecked(LABEL_FALSE)

                            if steps_obj.get_product_recommendation == "True":
                                self.product_recommendation_steps.setChecked(LABEL_TRUE)
                            else:
                                self.product_recommendation_steps.setChecked(
                                    LABEL_FALSE
                                )

                            if steps_obj.get_terms_and_condition == "True":
                                self.terms_and_condition_steps.setChecked(LABEL_TRUE)
                            else:
                                self.terms_and_condition_steps.setChecked(LABEL_FALSE)

                            if steps_obj.get_confirmation == "True":
                                self.confirmation_steps.setChecked(LABEL_TRUE)
                            else:
                                self.confirmation_steps.setChecked(LABEL_FALSE)

                            if steps_obj.get_is_paperless == "True":
                                self.is_paperless_steps.setChecked(LABEL_TRUE)
                            else:
                                self.is_paperless_steps.setChecked(LABEL_FALSE)

                            if (
                                steps_obj.get_user_id == "{dynamic}"
                                and steps_obj.get_both_step == "false"
                            ):
                                self.yes_login_group_box_steps.setChecked(LABEL_TRUE)
                            elif (
                                steps_obj.get_user_id == "{dynamic}"
                                and steps_obj.get_both_step == "true"
                            ):
                                self.both_login_group_box_steps.setChecked(LABEL_TRUE)
                            else:
                                self.no_login_group_box_steps.setChecked(LABEL_TRUE)

                            if steps_obj.get_event_error == "true":
                                self.yes_error_steps_group_box.setChecked(LABEL_TRUE)
                            else:
                                self.no_error_steps_group_box.setChecked(LABEL_TRUE)
                            break
            self.steps_edit = 0

    def delete_page_information(self):
        name = self.list_combo_box.currentText()
        page_delete_flag = 0
        for i in range(0, len(self.vrg.pages)):
            if self.application_type_combo.currentText() != APPLICATION_EMBER:
                if "page_name" in self.vrg.pages[i]:
                    if self.vrg.pages[i]["page_name"] == name:
                        del self.vrg.pages[i]
                        page_delete_flag = 1
                        break
            else:
                if "page_hierarchy" in self.vrg.pages[i]:
                    if self.vrg.pages[i]["page_hierarchy"] == name:
                        del self.vrg.pages[i]
                        page_delete_flag = 1
                        break

        if page_delete_flag == 0:
            for i in range(0, len(self.vrg.forms)):
                for j in range(0, len(self.vrg.forms[i]["steps"])):
                    if "step_name" in self.vrg.forms[i]["steps"][j]:
                        f1 = self.vrg.forms[i]["form_name"] + "-"
                        step_name_edit = str(name).replace(str(f1), "")
                        if (
                            self.vrg.forms[i]["steps"][j]["step_name"]
                            == step_name_edit
                        ):
                            if len(self.steps) > 0:
                                self.no_of_steps_form_box.setText(
                                    str(len(self.steps) - 1)
                                )
                                self.vrg.forms[i][
                                    "no_of_steps"
                                ] = self.no_of_steps_form_box.text()
                            if self.steps[i] == name:
                                del self.steps[i]
                            del self.vrg.forms[i]["steps"][j]
                            break

        self.list_combo_box.clear()
        page_delete_flag = 0
        if len(self.vrg.pages) > 0:
            for i in range(0, len(self.vrg.pages)):
                if self.application_type_combo.currentText() != APPLICATION_EMBER:
                    if "page_name" in self.vrg.pages[i]:
                        v1 = self.vrg.pages[i]["page_name"]
                        self.list_combo_box.addItem(v1)
                else:
                    if "page_hierarchy" in self.vrg.pages[i]:
                        v1 = self.vrg.pages[i]["page_hierarchy"]
                        self.list_combo_box.addItem(v1)

        if len(self.vrg.forms) > 0:
            for i in range(0, len(self.vrg.forms)):
                for j in range(0, len(self.vrg.forms[i]["steps"])):
                    if "step_name" in self.vrg.forms[i]["steps"][j]:
                        f1 = (
                            self.vrg.forms[i]["form_name"]
                            + "-"
                            + self.vrg.forms[i]["steps"][j]["step_name"]
                        )
                        self.list_combo_box.addItem(f1)

    def product_checkbox_button(self, product):
        if self.editFlag == 1:
            if product.isChecked():
                self.product_group_box_steps.setEnabled(LABEL_TRUE)
            else:
                self.product_group_box_steps.setEnabled(LABEL_FALSE)

    def transaction_checkbox_button(self, transaction):
        if self.editFlag == 1:
            if transaction.isChecked():
                self.transaction_group_box_steps.setEnabled(LABEL_TRUE)
            else:
                self.transaction_group_box_steps.setEnabled(LABEL_FALSE)

    def setup_ui(self, central):
        central.setObjectName("central")
        central.resize(1905, 985)
        central.setWindowIcon(QtGui.QIcon("cibc.png"))

        self.central_widget = QtWidgets.QWidget(central)
        self.central_widget.setObjectName("central_widget")

        self.application_title = QtWidgets.QLabel(self.central_widget)
        self.application_title.setGeometry(QtCore.QRect(380, 20, 211, 21))

        font = QtGui.QFont()
        font.setFamily(APPLICATION_FONT_STYLE)
        font.setPointSize(15)

        self.application_title.setFont(font)
        self.application_title.setObjectName("application_title")
        self.application_title.setGeometry(QtCore.QRect(380, 30, 500, 31))

        self.project_name_label = QtWidgets.QLabel(self.central_widget)
        self.project_name_label.setGeometry(QtCore.QRect(20, 70, 101, 28))
        self.project_name_label.setObjectName("project_name_label")

        self.project_name = QtWidgets.QLineEdit(self.central_widget)
        self.project_name.setGeometry(QtCore.QRect(150, 70, 231, 28))
        self.project_name.setObjectName("project_name")

        self.user_name_label = QtWidgets.QLabel(self.central_widget)
        self.user_name_label.setGeometry(QtCore.QRect(490, 70, 90, 28))
        self.user_name_label.setObjectName("user_name_label")

        self.user_name = QtWidgets.QLineEdit(self.central_widget)
        self.user_name.setGeometry(QtCore.QRect(620, 70, 241, 28))
        self.user_name.setObjectName("user_name")
        self.user_name.setText(os.getlogin())
        self.user_name.setEnabled(False)

        self.brand_label = QtWidgets.QLabel(self.central_widget)
        self.brand_label.setGeometry(QtCore.QRect(20, 130, 55, 28))
        self.brand_label.setObjectName("brand_label")

        self.brand_combo_box = QtWidgets.QComboBox(self.central_widget)
        self.brand_combo_box.setGeometry(QtCore.QRect(150, 130, 241, 28))
        self.brand_combo_box.setObjectName("brand_combo_box")
        self.brand_combo_box.addItem("")
        self.brand_combo_box.setItemText(0, "")
        self.brand_combo_box.addItem("")
        self.brand_combo_box.addItem("")
        self.brand_combo_box.addItem("")

        self.application_type_label = QtWidgets.QLabel(self.central_widget)
        self.application_type_label.setGeometry(QtCore.QRect(490, 130, 125, 28))
        self.application_type_label.setObjectName("application_type_label")

        self.application_type_combo = QtWidgets.QComboBox(self.central_widget)
        self.application_type_combo.setGeometry(QtCore.QRect(620, 130, 241, 28))
        self.application_type_combo.setObjectName("application_type_combo")
        self.application_type_combo.addItem("")
        self.application_type_combo.setItemText(0, "")
        self.application_type_combo.addItem("")
        self.application_type_combo.addItem("")
        self.application_type_combo.addItem("")
        self.application_type_combo.currentIndexChanged.connect(self.application_type)

        self.add_button = QtWidgets.QPushButton(self.central_widget)
        self.add_button.setGeometry(QtCore.QRect(100, 240, 93, 28))
        self.add_button.setObjectName("add_button")
        self.add_button.clicked.connect(self.add_page_button)

        self.add_flow = QtWidgets.QPushButton(self.central_widget)
        self.add_flow.setGeometry(QtCore.QRect(250, 240, 93, 28))
        self.add_flow.setObjectName("add_flow")
        self.add_flow.clicked.connect(self.add_flow_page)

        self.download_button = QtWidgets.QPushButton(self.central_widget)
        self.download_button.setGeometry(QtCore.QRect(400, 240, 124, 28))
        self.download_button.setObjectName("download_button")
        self.download_button.clicked.connect(self.download_button_page)

        self.interaction_button = QtWidgets.QPushButton(self.central_widget)
        self.interaction_button.setGeometry(QtCore.QRect(550, 240, 130, 28))
        self.interaction_button.setObjectName("interaction_button")
        self.interaction_button.clicked.connect(self.interaction_button_page)

        self.standalone_page_box = QtWidgets.QGroupBox(self.central_widget)
        self.standalone_page_box.setGeometry(QtCore.QRect(30, 290, 421, 351))
        self.standalone_page_box.setObjectName("standalone_page_box")

        self.page_name_standalone_label = QtWidgets.QLabel(self.standalone_page_box)
        self.page_name_standalone_label.setGeometry(QtCore.QRect(50, 40, 91, 28))
        self.page_name_standalone_label.setObjectName("page_name_standalone_label")

        self.page_name_standalone = QtWidgets.QLineEdit(self.standalone_page_box)
        self.page_name_standalone.setGeometry(QtCore.QRect(185, 40, 191, 28))
        self.page_name_standalone.setObjectName("page_name_standalone")

        self.page_hierarchy_standalone_label = QtWidgets.QLabel(
            self.standalone_page_box
        )
        self.page_hierarchy_standalone_label.setGeometry(QtCore.QRect(50, 80, 115, 28))
        self.page_hierarchy_standalone_label.setObjectName(
            "page_hierarchy_standalone_label"
        )

        self.page_hierarchy_standalone = QtWidgets.QLineEdit(self.standalone_page_box)
        self.page_hierarchy_standalone.setGeometry(QtCore.QRect(185, 80, 191, 28))
        self.page_hierarchy_standalone.setObjectName("page_hierarchy_standalone")

        self.error_group_box_standalone = QtWidgets.QGroupBox(self.standalone_page_box)
        self.error_group_box_standalone.setGeometry(QtCore.QRect(50, 115, 291, 61))
        self.error_group_box_standalone.setObjectName("error_group_box_standalone")

        self.yes_error_standalone = QtWidgets.QRadioButton(
            self.error_group_box_standalone
        )
        self.yes_error_standalone.setGeometry(QtCore.QRect(70, 20, 95, 20))
        self.yes_error_standalone.setObjectName("yes_error_standalone")

        self.no_error_standalone = QtWidgets.QRadioButton(
            self.error_group_box_standalone
        )
        self.no_error_standalone.setGeometry(QtCore.QRect(140, 20, 95, 20))
        self.no_error_standalone.setObjectName("no_error_standalone")

        self.login_group_box_page = QtWidgets.QGroupBox(self.standalone_page_box)
        self.login_group_box_page.setGeometry(QtCore.QRect(50, 180, 291, 80))
        self.login_group_box_page.setObjectName("login_group_box_page")

        self.yes_login_standalone = QtWidgets.QRadioButton(self.login_group_box_page)
        self.yes_login_standalone.setGeometry(QtCore.QRect(20, 30, 95, 20))
        self.yes_login_standalone.setObjectName("yes_login_standalone")

        self.no_login_standalone = QtWidgets.QRadioButton(self.login_group_box_page)
        self.no_login_standalone.setGeometry(QtCore.QRect(80, 30, 95, 20))
        self.no_login_standalone.setObjectName("no_login_standalone")

        self.both_login_standalone = QtWidgets.QRadioButton(self.login_group_box_page)
        self.both_login_standalone.setGeometry(QtCore.QRect(150, 30, 95, 20))
        self.both_login_standalone.setObjectName("both_login_standalone")

        self.save_button_standalone = QtWidgets.QPushButton(self.standalone_page_box)
        self.save_button_standalone.setGeometry(QtCore.QRect(50, 290, 93, 28))
        self.save_button_standalone.setObjectName("save_button_standalone")
        self.save_button_standalone.clicked.connect(self.save_standalone_page)

        self.cancel_button_standalone = QtWidgets.QPushButton(self.standalone_page_box)
        self.cancel_button_standalone.setGeometry(QtCore.QRect(200, 290, 93, 28))
        self.cancel_button_standalone.setObjectName("cancel_button_standalone")

        self.standalone_page_box.setEnabled(False)

        self.site_type_combo = QtWidgets.QComboBox(self.central_widget)
        self.site_type_combo.setGeometry(QtCore.QRect(150, 180, 241, 28))
        self.site_type_combo.setObjectName("site_type_combo")
        self.site_type_combo.addItem("")
        self.site_type_combo.setItemText(0, "")
        self.site_type_combo.addItem("")
        self.site_type_combo.addItem("")
        self.site_type_combo.addItem("")
        self.site_type_combo.currentIndexChanged.connect(self.site_type)

        self.site_type_label = QtWidgets.QLabel(self.central_widget)
        self.site_type_label.setGeometry(QtCore.QRect(20, 180, 81, 28))
        self.site_type_label.setObjectName("site_type_label")

        self.site_name_label = QtWidgets.QLabel(self.central_widget)
        self.site_name_label.setGeometry(QtCore.QRect(490, 180, 81, 28))
        self.site_name_label.setObjectName("site_name_label")

        self.site_name = QtWidgets.QLineEdit(self.central_widget)
        self.site_name.setGeometry(QtCore.QRect(620, 180, 241, 28))
        self.site_name.setObjectName("site_name")

        self.form_group_box = QtWidgets.QGroupBox(self.central_widget)
        self.form_group_box.setGeometry(QtCore.QRect(460, 290, 411, 351))
        self.form_group_box.setObjectName("form_group_box")

        self.form_name_label_form_box = QtWidgets.QLabel(self.form_group_box)
        self.form_name_label_form_box.setGeometry(QtCore.QRect(30, 50, 91, 28))
        self.form_name_label_form_box.setObjectName("form_name_label_form_box")

        self.form_name_form_box = QtWidgets.QLineEdit(self.form_group_box)
        self.form_name_form_box.setGeometry(QtCore.QRect(150, 50, 201, 28))
        self.form_name_form_box.setObjectName("form_name_form_box")

        self.no_of_steps_label_form_box = QtWidgets.QLabel(self.form_group_box)
        self.no_of_steps_label_form_box.setGeometry(QtCore.QRect(30, 130, 93, 28))
        self.no_of_steps_label_form_box.setObjectName("no_of_steps_label_form_box")

        self.no_of_steps_form_box = QtWidgets.QLineEdit(self.form_group_box)
        self.no_of_steps_form_box.setGeometry(QtCore.QRect(150, 120, 201, 28))
        self.no_of_steps_form_box.setObjectName("no_of_steps_form_box")

        self.product_checkbox_form_box = QtWidgets.QCheckBox(self.form_group_box)
        self.product_checkbox_form_box.setGeometry(QtCore.QRect(50, 200, 84, 20))
        self.product_checkbox_form_box.setObjectName("product_checkbox_form_box")
        self.product_checkbox_form_box.stateChanged.connect(
            lambda: self.product_checkbox_button(self.product_checkbox_form_box)
        )

        self.transaction_checkbox_form_box = QtWidgets.QCheckBox(self.form_group_box)
        self.transaction_checkbox_form_box.setGeometry(QtCore.QRect(160, 200, 111, 20))
        self.transaction_checkbox_form_box.setObjectName(
            "transaction_checkbox_form_box"
        )
        self.transaction_checkbox_form_box.stateChanged.connect(
            lambda: self.transaction_checkbox_button(self.transaction_checkbox_form_box)
        )

        self.generate_steps_form_box = QtWidgets.QPushButton(self.form_group_box)
        self.generate_steps_form_box.setGeometry(QtCore.QRect(120, 260, 121, 28))
        self.generate_steps_form_box.setObjectName("generate_steps_form_box")
        self.generate_steps_form_box.clicked.connect(self.save_form_page)

        self.form_group_box.setEnabled(False)

        self.step_group_box = QtWidgets.QGroupBox(self.central_widget)
        self.step_group_box.setGeometry(QtCore.QRect(890, 20, 1001, 791))
        self.step_group_box.setObjectName("step_group_box")

        self.page_name_label_steps = QtWidgets.QLabel(self.step_group_box)
        self.page_name_label_steps.setGeometry(QtCore.QRect(50, 40, 91, 28))
        self.page_name_label_steps.setObjectName("page_name_label_steps")

        self.page_name_steps = QtWidgets.QLineEdit(self.step_group_box)
        self.page_name_steps.setGeometry(QtCore.QRect(140, 40, 181, 28))
        self.page_name_steps.setObjectName("page_name_steps")

        self.step_name_label_steps = QtWidgets.QLabel(self.step_group_box)
        self.step_name_label_steps.setGeometry(QtCore.QRect(520, 30, 115, 28))
        self.step_name_label_steps.setObjectName("step_name_label_steps")

        self.step_name_steps = QtWidgets.QLineEdit(self.step_group_box)
        self.step_name_steps.setGeometry(QtCore.QRect(640, 30, 200, 28))
        self.step_name_steps.setObjectName("step_name_steps")

        self.page_hierarchy_label_steps = QtWidgets.QLabel(self.step_group_box)
        self.page_hierarchy_label_steps.setGeometry(QtCore.QRect(520, 80, 115, 28))
        self.page_hierarchy_label_steps.setObjectName("page_hierarchy_label_steps")

        self.page_hierarchy_steps = QtWidgets.QLineEdit(self.step_group_box)
        self.page_hierarchy_steps.setGeometry(QtCore.QRect(640, 80, 200, 28))
        self.page_hierarchy_steps.setObjectName("page_hierarchy_steps")

        self.login_group_box_steps = QtWidgets.QGroupBox(self.step_group_box)
        self.login_group_box_steps.setGeometry(QtCore.QRect(50, 90, 351, 91))
        self.login_group_box_steps.setObjectName("login_group_box_steps")

        self.yes_login_group_box_steps = QtWidgets.QRadioButton(
            self.login_group_box_steps
        )
        self.yes_login_group_box_steps.setGeometry(QtCore.QRect(10, 40, 95, 20))
        self.yes_login_group_box_steps.setObjectName("yes_login_group_box_steps")

        self.no_login_group_box_steps = QtWidgets.QRadioButton(
            self.login_group_box_steps
        )
        self.no_login_group_box_steps.setGeometry(QtCore.QRect(110, 40, 95, 20))
        self.no_login_group_box_steps.setObjectName("no_login_group_box_steps")

        self.both_login_group_box_steps = QtWidgets.QRadioButton(
            self.login_group_box_steps
        )
        self.both_login_group_box_steps.setGeometry(QtCore.QRect(220, 40, 95, 20))
        self.both_login_group_box_steps.setObjectName("both_login_group_box_steps")

        self.form_group_box_steps = QtWidgets.QGroupBox(self.step_group_box)
        self.form_group_box_steps.setGeometry(QtCore.QRect(470, 230, 531, 91))
        self.form_group_box_steps.setObjectName("form_group_box_steps")

        self.form_view_steps = QtWidgets.QCheckBox(self.form_group_box_steps)
        self.form_view_steps.setGeometry(QtCore.QRect(130, 20, 121, 20))
        self.form_view_steps.setObjectName("form_view_steps")

        self.form_submit_steps = QtWidgets.QCheckBox(self.form_group_box_steps)
        self.form_submit_steps.setGeometry(QtCore.QRect(130, 60, 121, 20))
        self.form_submit_steps.setObjectName("form_submit_steps")

        self.form_qualify_steps = QtWidgets.QCheckBox(self.form_group_box_steps)
        self.form_qualify_steps.setGeometry(QtCore.QRect(390, 20, 161, 20))
        self.form_qualify_steps.setObjectName("form_qualify_steps")

        self.form_steps = QtWidgets.QCheckBox(self.form_group_box_steps)
        self.form_steps.setGeometry(QtCore.QRect(390, 60, 101, 20))
        self.form_steps.setObjectName("form_steps")

        self.error_form_group_box_steps = QtWidgets.QGroupBox(self.form_group_box_steps)
        self.error_form_group_box_steps.setGeometry(QtCore.QRect(630, 90, 301, 80))
        self.error_form_group_box_steps.setObjectName("error_form_group_box_steps")

        self.yes_error_form_group_box_steps = QtWidgets.QRadioButton(
            self.error_form_group_box_steps
        )
        self.yes_error_form_group_box_steps.setGeometry(QtCore.QRect(40, 30, 95, 20))
        self.yes_error_form_group_box_steps.setObjectName(
            "yes_error_form_group_box_steps"
        )

        self.no_error_form_group_box_steps = QtWidgets.QRadioButton(
            self.error_form_group_box_steps
        )
        self.no_error_form_group_box_steps.setGeometry(QtCore.QRect(120, 30, 95, 20))
        self.no_error_form_group_box_steps.setObjectName(
            "no_error_form_group_box_steps"
        )

        self.product_group_box_steps = QtWidgets.QGroupBox(self.step_group_box)
        self.product_group_box_steps.setGeometry(QtCore.QRect(40, 400, 971, 301))
        self.product_group_box_steps.setObjectName("product_group_box_steps")

        self.product_app_group_box_steps = QtWidgets.QGroupBox(
            self.product_group_box_steps
        )
        self.product_app_group_box_steps.setGeometry(QtCore.QRect(30, 140, 891, 131))
        self.product_app_group_box_steps.setObjectName("product_app_group_box_steps")

        self.personal_details_steps = QtWidgets.QCheckBox(
            self.product_app_group_box_steps
        )
        self.personal_details_steps.setGeometry(QtCore.QRect(80, 30, 210, 20))
        self.personal_details_steps.setObjectName("personal_details_steps")

        self.summary_steps = QtWidgets.QCheckBox(self.product_app_group_box_steps)
        self.summary_steps.setGeometry(QtCore.QRect(340, 30, 120, 21))
        self.summary_steps.setObjectName("summary_steps")

        self.confirmation_steps = QtWidgets.QCheckBox(self.product_app_group_box_steps)
        self.confirmation_steps.setGeometry(QtCore.QRect(550, 30, 131, 20))
        self.confirmation_steps.setObjectName("confirmation_steps")

        self.product_recommendation_steps = QtWidgets.QCheckBox(
            self.product_app_group_box_steps
        )
        self.product_recommendation_steps.setGeometry(QtCore.QRect(80, 60, 210, 20))
        self.product_recommendation_steps.setObjectName("product_recommendation_steps")

        self.terms_and_condition_steps = QtWidgets.QCheckBox(
            self.product_app_group_box_steps
        )
        self.terms_and_condition_steps.setGeometry(QtCore.QRect(340, 60, 180, 20))
        self.terms_and_condition_steps.setObjectName("terms_and_condition_steps")

        self.is_paperless_steps = QtWidgets.QCheckBox(self.product_app_group_box_steps)
        self.is_paperless_steps.setGeometry(QtCore.QRect(550, 60, 131, 20))
        self.is_paperless_steps.setObjectName("is_paperless_steps")

        self.product_id_label_steps = QtWidgets.QLabel(self.product_group_box_steps)
        self.product_id_label_steps.setGeometry(QtCore.QRect(10, 40, 91, 28))
        self.product_id_label_steps.setObjectName("product_id_label_steps")

        self.product_id_steps = QtWidgets.QLineEdit(self.product_group_box_steps)
        self.product_id_steps.setGeometry(QtCore.QRect(110, 40, 161, 28))
        self.product_id_steps.setObjectName("product_id_steps")

        self.parent_product_label_steps = QtWidgets.QLabel(self.product_group_box_steps)
        self.parent_product_label_steps.setGeometry(QtCore.QRect(300, 40, 121, 28))
        self.parent_product_label_steps.setObjectName("parent_product_label_steps")

        self.parent_product_steps = QtWidgets.QLineEdit(self.product_group_box_steps)
        self.parent_product_steps.setGeometry(QtCore.QRect(430, 40, 181, 28))
        self.parent_product_steps.setObjectName("parent_product_steps")

        self.adjudication_label_steps = QtWidgets.QLabel(self.product_group_box_steps)
        self.adjudication_label_steps.setGeometry(QtCore.QRect(640, 40, 130, 28))
        self.adjudication_label_steps.setObjectName("adjudication_label_steps")

        self.adjudication_steps = QtWidgets.QLineEdit(self.product_group_box_steps)
        self.adjudication_steps.setGeometry(QtCore.QRect(740, 40, 181, 28))
        self.adjudication_steps.setObjectName("adjudication_steps")

        self.positioning_label_steps = QtWidgets.QLabel(self.product_group_box_steps)
        self.positioning_label_steps.setGeometry(QtCore.QRect(10, 90, 111, 28))
        self.positioning_label_steps.setObjectName("positioning_label_steps")

        self.positioning_combo_box_steps = QtWidgets.QComboBox(
            self.product_group_box_steps
        )
        self.positioning_combo_box_steps.setGeometry(QtCore.QRect(110, 90, 161, 28))
        self.positioning_combo_box_steps.setObjectName("positioning_combo_box_steps")
        self.positioning_combo_box_steps.addItem("")
        self.positioning_combo_box_steps.addItem("")
        self.positioning_combo_box_steps.addItem("")
        self.positioning_combo_box_steps.addItem("")
        self.positioning_combo_box_steps.addItem("")
        self.positioning_combo_box_steps.addItem("")

        self.grouping_label_steps = QtWidgets.QLabel(self.product_group_box_steps)
        self.grouping_label_steps.setGeometry(QtCore.QRect(300, 90, 160, 28))
        self.grouping_label_steps.setObjectName("grouping_label_steps")

        self.grouping_combo_box = QtWidgets.QComboBox(self.product_group_box_steps)
        self.grouping_combo_box.setGeometry(QtCore.QRect(430, 90, 181, 28))
        self.grouping_combo_box.setObjectName("grouping_combobox")
        self.grouping_combo_box.addItem("")
        self.grouping_combo_box.addItem("")
        self.grouping_combo_box.addItem("")
        self.grouping_combo_box.addItem("")

        self.fulfillment_label_steps = QtWidgets.QLabel(self.product_group_box_steps)
        self.fulfillment_label_steps.setGeometry(QtCore.QRect(640, 90, 180, 28))
        self.fulfillment_label_steps.setObjectName("fulfillment_label_steps")

        self.fulfillment_combo_box_steps = QtWidgets.QComboBox(
            self.product_group_box_steps
        )
        self.fulfillment_combo_box_steps.setGeometry(QtCore.QRect(740, 90, 180, 28))
        self.fulfillment_combo_box_steps.setObjectName("fulfillment_combo_box_steps")
        self.fulfillment_combo_box_steps.addItem("")
        self.fulfillment_combo_box_steps.addItem("")
        self.fulfillment_combo_box_steps.addItem("")
        self.fulfillment_combo_box_steps.addItem("")
        self.fulfillment_combo_box_steps.addItem("")
        self.fulfillment_combo_box_steps.addItem("")

        self.transaction_group_box_steps = QtWidgets.QGroupBox(self.step_group_box)
        self.transaction_group_box_steps.setGeometry(QtCore.QRect(50, 190, 351, 191))
        self.transaction_group_box_steps.setObjectName("transaction_group_box_steps")

        self.from_label_steps = QtWidgets.QLabel(self.transaction_group_box_steps)
        self.from_label_steps.setGeometry(QtCore.QRect(40, 40, 55, 28))
        self.from_label_steps.setObjectName("from_label_steps")

        self.from_text_steps = QtWidgets.QLineEdit(self.transaction_group_box_steps)
        self.from_text_steps.setGeometry(QtCore.QRect(130, 40, 151, 28))
        self.from_text_steps.setObjectName("from_text_steps")

        self.to_label_steps = QtWidgets.QLabel(self.transaction_group_box_steps)
        self.to_label_steps.setGeometry(QtCore.QRect(40, 90, 55, 28))
        self.to_label_steps.setObjectName("to_label_steps")

        self.to_text_steps = QtWidgets.QLineEdit(self.transaction_group_box_steps)
        self.to_text_steps.setGeometry(QtCore.QRect(130, 90, 151, 28))
        self.to_text_steps.setObjectName("to_text_steps")

        self.is_external_check_box_steps = QtWidgets.QCheckBox(
            self.transaction_group_box_steps
        )
        self.is_external_check_box_steps.setGeometry(QtCore.QRect(130, 140, 141, 20))
        self.is_external_check_box_steps.setObjectName("is_external_check_box_steps")

        self.error_steps_group_box = QtWidgets.QGroupBox(self.step_group_box)
        self.error_steps_group_box.setGeometry(QtCore.QRect(510, 110, 411, 101))
        self.error_steps_group_box.setObjectName("error_steps_group_box")

        self.yes_error_steps_group_box = QtWidgets.QRadioButton(
            self.error_steps_group_box
        )
        self.yes_error_steps_group_box.setGeometry(QtCore.QRect(50, 50, 95, 20))
        self.yes_error_steps_group_box.setObjectName("yes_error_steps_group_box")

        self.no_error_steps_group_box = QtWidgets.QRadioButton(
            self.error_steps_group_box
        )
        self.no_error_steps_group_box.setGeometry(QtCore.QRect(170, 50, 95, 20))
        self.no_error_steps_group_box.setObjectName("no_error_steps_group_box")

        self.save_and_next_steps = QtWidgets.QPushButton(self.step_group_box)
        self.save_and_next_steps.setGeometry(QtCore.QRect(380, 720, 93, 28))
        self.save_and_next_steps.setObjectName("save_and_next_steps")
        self.save_and_next_steps.clicked.connect(self.save_steps_information)

        self.cancel_steps = QtWidgets.QPushButton(self.step_group_box)
        self.cancel_steps.setGeometry(QtCore.QRect(510, 720, 93, 28))
        self.cancel_steps.setObjectName("cancel_steps")

        self.step_group_box.setEnabled(False)

        self.download_group_box = QtWidgets.QGroupBox(self.central_widget)
        self.download_group_box.setGeometry(QtCore.QRect(40, 650, 400, 190))
        self.download_group_box.setObjectName("download_group_box")

        self.download_label = QtWidgets.QLabel(self.download_group_box)
        self.download_label.setGeometry(QtCore.QRect(30, 50, 130, 28))
        self.download_label.setObjectName("download_label")

        self.download_name = QtWidgets.QLineEdit(self.download_group_box)
        self.download_name.setGeometry(QtCore.QRect(160, 50, 180, 28))
        self.download_name.setObjectName("download_name")

        self.download_type_label = QtWidgets.QLabel(self.download_group_box)
        self.download_type_label.setGeometry(QtCore.QRect(30, 100, 180, 28))
        self.download_type_label.setObjectName("download_type_label")

        self.download_type_combo_box = QtWidgets.QComboBox(self.download_group_box)
        self.download_type_combo_box.setGeometry(QtCore.QRect(160, 100, 180, 28))
        self.download_type_combo_box.setObjectName("download_type_combo_box")
        self.download_type_combo_box.addItem("")
        self.download_type_combo_box.addItem("")
        self.download_type_combo_box.addItem("")
        self.download_type_combo_box.addItem("")

        self.download_save_button = QtWidgets.QPushButton(self.download_group_box)
        self.download_save_button.setGeometry(QtCore.QRect(180, 150, 93, 28))
        self.download_save_button.setObjectName("download_save_button")
        self.download_save_button.clicked.connect(self.save_download_information)

        self.download_group_box.setEnabled(LABEL_FALSE)

        self.interaction_group_box = QtWidgets.QGroupBox(self.central_widget)
        self.interaction_group_box.setGeometry(QtCore.QRect(450, 650, 400, 190))
        self.interaction_group_box.setObjectName("interaction_group_box")

        self.interaction_label = QtWidgets.QLabel(self.interaction_group_box)
        self.interaction_label.setGeometry(QtCore.QRect(30, 50, 130, 28))
        self.interaction_label.setObjectName("interaction_label")

        self.interaction_name = QtWidgets.QLineEdit(self.interaction_group_box)
        self.interaction_name.setGeometry(QtCore.QRect(160, 50, 180, 28))
        self.interaction_name.setObjectName("interaction_name")

        self.interaction_save_button = QtWidgets.QPushButton(self.interaction_group_box)
        self.interaction_save_button.setGeometry(QtCore.QRect(180, 150, 100, 28))
        self.interaction_save_button.setObjectName("interaction_save_button")
        self.interaction_save_button.clicked.connect(self.save_interaction_information)

        self.interaction_group_box.setEnabled(False)

        self.list_group_box = QtWidgets.QGroupBox(self.central_widget)
        self.list_group_box.setGeometry(QtCore.QRect(40, 850, 810, 100))
        self.list_group_box.setObjectName("list_group_box")

        self.list_combo_box = QtWidgets.QComboBox(self.list_group_box)
        self.list_combo_box.setGeometry(QtCore.QRect(30, 50, 370, 30))
        self.list_combo_box.setObjectName("list_combo_box")

        self.list_edit_button = QtWidgets.QPushButton(self.list_group_box)
        self.list_edit_button.setGeometry(QtCore.QRect(450, 50, 100, 28))
        self.list_edit_button.setObjectName("list_edit_button")
        self.list_edit_button.clicked.connect(self.edit_list_box_button)

        self.list_delete_button = QtWidgets.QPushButton(self.list_group_box)
        self.list_delete_button.setGeometry(QtCore.QRect(600, 50, 100, 28))
        self.list_delete_button.setObjectName("list_delete_button")
        self.list_delete_button.clicked.connect(self.delete_page_information)

        self.generate_vrg_button = QtWidgets.QPushButton(self.central_widget)
        self.generate_vrg_button.setGeometry(QtCore.QRect(1200, 900, 120, 28))
        self.generate_vrg_button.setObjectName("generate_vrg_button")
        self.generate_vrg_button.clicked.connect(self.generate_button)

        self.close_vrg_button = QtWidgets.QPushButton(self.central_widget)
        self.close_vrg_button.setGeometry(QtCore.QRect(1400, 900, 120, 28))
        self.close_vrg_button.setObjectName("close_vrg_button")
        self.close_vrg_button.clicked.connect(self.close_button)

        self.reset_button = QtWidgets.QPushButton(self.central_widget)
        self.reset_button.setGeometry(QtCore.QRect(1550, 900, 120, 28))
        self.reset_button.setObjectName("reset_button")
        self.reset_button.clicked.connect(self.reset)

        central.setCentralWidget(self.central_widget)

        self.menu_bar = QtWidgets.QMenuBar(central)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 1905, 26))
        self.menu_bar.setObjectName("menu_bar")
        central.setMenuBar(self.menu_bar)
        self.status_bar = QtWidgets.QStatusBar(central)
        self.status_bar.setObjectName("status_bar")
        central.setStatusBar(self.status_bar)

        self.re_translate_ui(central)
        QtCore.QMetaObject.connectSlotsByName(central)

    def re_translate_ui(self, central):
        translate = QtCore.QCoreApplication.translate
        central.setWindowTitle(translate("central", APPLICATION_TITLE))
        self.application_title.setText(translate("central", APPLICATION_NAME))
        self.project_name_label.setText(translate("central", LABEL_PROJECT_NAME))
        self.user_name_label.setText(translate("central", LABEL_PREPARED_BY))
        self.brand_label.setText(translate("central", LABEL_BRAND_NAME))
        self.brand_combo_box.setItemText(1, translate("central", LABEL_CIBC))
        self.brand_combo_box.setItemText(2, translate("central", LABEL_CIBC_US))
        self.brand_combo_box.setItemText(3, translate("central", LABEL_SIMPLII))
        self.application_type_label.setText(
            translate("central", LABEL_APPLICATION_TYPE)
        )
        self.application_type_combo.setItemText(
            1, translate("central", APPLICATION_EMBER)
        )
        self.application_type_combo.setItemText(
            2, translate("central", APPLICATION_ANGULAR)
        )
        self.application_type_combo.setItemText(
            3, translate("central", APPLICATION_MOBILE_JSON)
        )
        self.site_type_combo.setItemText(1, translate("central", LABEL_DESKTOP))
        self.site_type_combo.setItemText(2, translate("central", LABEL_MOBILE))
        self.site_type_combo.setItemText(3, translate("central", LABEL_RESPONSIVE))
        self.site_type_label.setText(translate("central", LABEL_SITE_TYPE))
        self.site_name_label.setText(translate("central", LABEL_SITE_NAME))

        self.add_button.setText(translate("central", LABEL_ADD_PAGE))
        self.add_flow.setText(translate("central", LABEL_ADD_FLOW))
        self.download_button.setText(translate("central", LABEL_ADD_DOWNLOAD))
        self.interaction_button.setText(translate("central", LABEL_ADD_INTERACTION))

        self.standalone_page_box.setTitle(translate("central", LABEL_STANDALONE_PAGE))
        self.page_name_standalone_label.setText(translate("central", LABEL_PAGE_NAME))
        self.page_hierarchy_standalone_label.setText(
            translate("central", LABEL_PAGE_HIERARCHY)
        )
        self.error_group_box_standalone.setTitle(translate("central", LABEL_ERROR))
        self.yes_error_standalone.setText(translate("central", LABEL_YES))
        self.no_error_standalone.setText(translate("central", LABEL_NO))
        self.login_group_box_page.setTitle(translate("central", LABEL_LOGIN))
        self.yes_login_standalone.setText(translate("central", LABEL_YES))
        self.no_login_standalone.setText(translate("central", LABEL_NO))
        self.both_login_standalone.setText(translate("central", LABEL_BOTH))
        self.save_button_standalone.setText(translate("central", LABEL_SAVE))
        self.cancel_button_standalone.setText(translate("central", LABEL_CANCEL))

        self.form_group_box.setTitle(translate("central", LABEL_FORM_FLOW))
        self.form_name_label_form_box.setText(translate("central", LABEL_FORM_NAME))
        self.no_of_steps_label_form_box.setText(translate("central", LABEL_NO_OF_STEPS))
        self.product_checkbox_form_box.setText(translate("central", LABEL_PRODUCTS))
        self.transaction_checkbox_form_box.setText(
            translate("central", LABEL_TRANSACTION)
        )
        self.generate_steps_form_box.setText(translate("central", LABEL_GENERATE_STEPS))

        self.step_group_box.setTitle(translate("central", LABEL_STEPS))
        self.page_name_label_steps.setText(translate("central", LABEL_PAGE_NAME))
        self.step_name_label_steps.setText(translate("central", LABEL_STEP_NAME))
        self.page_hierarchy_label_steps.setText(
            translate("central", LABEL_PAGE_HIERARCHY)
        )
        self.login_group_box_steps.setTitle(translate("central", LABEL_LOGIN))
        self.yes_login_group_box_steps.setText(translate("central", LABEL_YES))
        self.no_login_group_box_steps.setText(translate("central", LABEL_NO))
        self.both_login_group_box_steps.setText(translate("central", LABEL_BOTH))
        self.form_group_box.setTitle(translate("central", LABEL_FORM_STEPS))
        self.form_view_steps.setText(translate("central", LABEL_FORM_VIEW))
        self.form_submit_steps.setText(translate("central", LABEL_FORM_SUBMIT))
        self.form_qualify_steps.setText(translate("central", LABEL_FORM_QUALIFY))
        self.form_steps.setText(translate("central", LABEL_FORM_STEPS))
        self.error_form_group_box_steps.setTitle(translate("central", LABEL_ERROR))
        self.yes_error_form_group_box_steps.setText(translate("central", LABEL_YES))
        self.no_error_form_group_box_steps.setText(translate("central", LABEL_NO))
        self.product_group_box_steps.setTitle(
            translate("central", LABEL_PRODUCT_INFORMATION)
        )
        self.product_app_group_box_steps.setTitle(
            translate("central", LABEL_PRODUCT_APPLICATION_STEPS)
        )
        self.personal_details_steps.setText(
            translate("central", LABEL_PERSONAL_DETAILS)
        )
        self.summary_steps.setText(translate("central", LABEL_SUMMARY))
        self.confirmation_steps.setText(translate("central", LABEL_CONFIRMATION))
        self.product_recommendation_steps.setText(
            translate("central", LABEL_PRODUCT_RECOMMENDATION)
        )
        self.terms_and_condition_steps.setText(
            translate("central", LABEL_TERMS_AND_CONDITION)
        )
        self.is_paperless_steps.setText(translate("central", LABEL_IS_PAPERLESS))
        self.product_id_label_steps.setText(translate("central", LABEL_PRODUCT_ID))
        self.parent_product_label_steps.setText(
            translate("central", LABEL_PARENT_PRODUCT)
        )
        self.adjudication_label_steps.setText(translate("central", LABEL_ADJUDICATION))
        self.positioning_label_steps.setText(translate("central", LABEL_POSTIONING))
        self.positioning_combo_box_steps.setItemText(
            0, translate("central", LABEL_NOT_APPLICABLE)
        )
        self.positioning_combo_box_steps.setItemText(
            1, translate("central", LABEL_UP_SELL)
        )
        self.positioning_combo_box_steps.setItemText(
            2, translate("central", LABEL_DOWN_SELL)
        )
        self.positioning_combo_box_steps.setItemText(
            3, translate("central", LABEL_USER_SELECTED)
        )
        self.positioning_combo_box_steps.setItemText(
            4, translate("central", LABEL_SYSTEM_RECOMMENDED)
        )
        self.positioning_combo_box_steps.setItemText(
            5, translate("central", LABEL_DYNAMIC)
        )
        self.grouping_label_steps.setText(translate("central", LABEL_GROUPING))
        self.grouping_combo_box.setItemText(
            0, translate("central", LABEL_NOT_APPLICABLE)
        )
        self.grouping_combo_box.setItemText(1, translate("central", LABEL_BUNDLE_ID))
        self.grouping_combo_box.setItemText(2, translate("central", LABEL_NO_GROUPING))
        self.grouping_combo_box.setItemText(3, translate("central", LABEL_DYNAMIC))
        self.fulfillment_label_steps.setText(translate("central", LABEL_FULFILLMENT))
        self.fulfillment_combo_box_steps.setItemText(
            0, translate("central", LABEL_NOT_APPLICABLE)
        )
        self.fulfillment_combo_box_steps.setItemText(
            1, translate("central", LABEL_BRANCH)
        )
        self.fulfillment_combo_box_steps.setItemText(
            2, translate("central", LABEL_ESIG)
        )
        self.fulfillment_combo_box_steps.setItemText(3, translate("central", LABEL_RDC))
        self.fulfillment_combo_box_steps.setItemText(
            4, translate("central", LABEL_DIRECT)
        )
        self.fulfillment_combo_box_steps.setItemText(
            5, translate("central", LABEL_DYNAMIC)
        )
        self.transaction_group_box_steps.setTitle(
            translate("central", LABEL_TRANSACTION)
        )
        self.from_label_steps.setText(translate("central", LABEL_FROM))
        self.to_label_steps.setText(translate("central", LABEL_TO))
        self.is_external_check_box_steps.setText(
            translate("central", LABEL_IS_EXTERNAL)
        )

        self.error_steps_group_box.setTitle(translate("central", LABEL_ERROR))
        self.yes_error_steps_group_box.setText(translate("central", LABEL_YES))
        self.no_error_steps_group_box.setText(translate("central", LABEL_NO))

        self.save_and_next_steps.setText(translate("central", LABEL_SAVE_NEXT))
        self.cancel_steps.setText(translate("central", LABEL_CANCEL))
        self.generate_vrg_button.setText(translate("central", LABEL_GENERATE_VRG))
        self.close_vrg_button.setText(translate("central", LABEL_CLOSE))
        self.reset_button.setText(translate("central", LABEL_RESET))

        self.download_group_box.setTitle(translate("central", LABEL_DOWNLOAD))
        self.download_type_label.setText(translate("central", LABEL_FILE_TYPE))
        self.download_type_combo_box.setItemText(0, translate("central", LABEL_BLANK))
        self.download_type_combo_box.setItemText(1, translate("central", LABEL_PDF))
        self.download_type_combo_box.setItemText(2, translate("central", LABEL_JPEG))
        self.download_type_combo_box.setItemText(3, translate("central", LABEL_OTHER))
        self.download_label.setText(translate("central", LABEL_FILE_NAME))
        self.download_save_button.setText(translate("central", LABEL_SAVE))

        self.interaction_group_box.setTitle(translate("central", LABEL_INTERACTION))
        self.interaction_label.setText(translate("central", LABEL_INTERACTION_NAME))
        self.interaction_save_button.setText(translate("central", LABEL_SAVE))

        self.list_group_box.setTitle(translate("central", LABEL_LIST_OF_PAGES))
        self.list_edit_button.setText(translate("central", LABEL_EDIT))
        self.list_delete_button.setText(translate("central", LABEL_DELETE))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    c = QtWidgets.QMainWindow()
    ui = VRGAutomation()
    userName = os.getlogin()
    ui.setup_ui(c)
    c.show()
    sys.exit(app.exec_())
