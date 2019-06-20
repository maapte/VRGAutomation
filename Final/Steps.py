"""
__author__ : Manish Apte
__maintainer__ : Manish Apte
__organization__ : Deloitte
"""


class Steps:

    def __init__(self):
        self.page_view = "true"
        self.page_path = "{dynamic}"
        self.page_name = ""
        self.page_url = "{dynamic}"
        self.page_referrer = "{dynamic}"
        self.page_hierarchy = "{dynamic}"
        self.page_language = "{en|fr}"
        self.page_accessibility = "true"
        self.page_login = ""

        self.step_name = ""
        self.form_step = "true"
        self.form_view = ""
        self.form_submit = ""
        self.form_qualify = ""
        self.unique_id = "{dynamic}"

        self.transaction_id = ""
        self.transaction_amount = ""
        self.transaction_service_fee = ""
        self.transaction_unit = ""
        self.from_transaction = ""
        self.to_transaction = ""
        self.is_external = ""
        self.is_transaction_complete = ""

        self.product_information = ""
        self.product_id = ""
        self.parent_product = ""
        self.adjudication = ""
        self.product_positioning = ""
        self.product_grouping = ""
        self.fulfillment = ""
        self.product_application_step = ""
        self.personal_details = ""
        self.summary = ""
        self.confirmation = ""
        self.product_recommendation = ""
        self.terms_and_condition = ""
        self.is_paperless = ""

        self.user_id = ""
        self.user_type = ""
        self.user_auth_state = ""

        self.event_error = "false"
        self.error_message = ""
        self.error_type = ""
        self.error_sub_type = ""
        self.error_field = ""
        self.error_code = ""

        self.login_event = ""
        self.advertising = "false"
        self.events_advertising = ""
        self.events_ad_click = ""
        self.advertising_tracking_code = ""
        self.advertising_location = ""
        self.advertising_type = ""
        self.is_login = "false"
        self.is_otvc = "false"
        self.is_joint = "false"
        self.is_otvc_prompt_steps = ""
        self.is_otvc_success_steps = ""

    @property
    def get_page_name(self):
        return self.page_name

    def set_page_name(self, page_name):
        self.page_name = page_name

    @property
    def get_page_referrer(self):
        return self.page_referrer

    def set_page_referrer(self, page_referrer):
        self.page_referrer = page_referrer

    @property
    def get_page_language(self):
        return self.page_language

    def set_page_language(self, page_language):
        self.page_language = page_language

    @property
    def get_page_view(self):
        return self.page_view

    def set_page_view(self, page_view):
        self.page_view = page_view

    @property
    def get_page_accessibility(self):
        return self.page_accessibility

    def set_page_accessibility(self, page_accessibility):
        self.page_accessibility = page_accessibility

    @property
    def get_page_hierarchy(self):
        return self.page_hierarchy

    def set_page_hierarchy(self, page_hierarchy):
        self.page_hierarchy = page_hierarchy

    @property
    def get_page_path(self):
        return self.page_path

    def set_page_path(self, page_path):
        self.page_path = page_path

    @property
    def get_page_url(self):
        return self.page_url

    def set_page_url(self, page_url):
        self.page_url = page_url

    @property
    def get_is_external(self):
        return self.is_external

    def set_is_external(self, is_external):
        self.is_external = is_external

    @property
    def get_is_transaction_complete(self):
        return self.is_transaction_complete

    def set_is_transaction_complete(self, is_transaction_complete):
        self.is_transaction_complete = is_transaction_complete

    @property
    def get_transaction_id(self):
        return self.transaction_id

    def set_transaction_id(self, transaction_id):
        self.transaction_id = transaction_id

    @property
    def get_transaction_amount(self):
        return self.transaction_amount

    def set_transaction_amount(self, transaction_amount):
        self.transaction_amount = transaction_amount

    @property
    def get_transaction_service_fee(self):
        return self.transaction_service_fee

    def set_transaction_service_fee(self, transaction_service_fee):
        self.transaction_service_fee = transaction_service_fee

    @property
    def get_transaction_unit(self):
        return self.transaction_unit

    def set_transaction_unit(self, transaction_unit):
        self.transaction_unit = transaction_unit

    @property
    def get_from_transaction(self):
        return self.from_transaction

    def set_from_transaction(self, from_transaction):
        self.from_transaction = from_transaction

    @property
    def get_to_transaction(self):
        return self.to_transaction

    def set_to_transaction(self, to_transaction):
        self.to_transaction = to_transaction

    @property
    def get_step_name(self):
        return self.step_name

    def set_step_name(self, step_name):
        self.step_name = step_name

    @property
    def get_form_step(self):
        return self.form_step

    def set_form_step(self, form_step):
        self.form_step = form_step

    @property
    def get_form_view(self):
        return self.form_view

    def set_form_view(self, form_view):
        self.form_view = form_view

    @property
    def get_form_submit(self):
        return self.form_submit

    def set_form_submit(self, form_submit):
        self.form_submit = form_submit

    @property
    def get_form_qualify(self):
        return self.form_qualify

    def set_form_qualify(self, form_qualify):
        self.form_qualify = form_qualify

    @property
    def get_unique_id(self):
        return self.unique_id

    def set_unique_id(self, unique_id):
        self.unique_id = unique_id

    @property
    def get_page_login(self):
        return self.page_login

    def set_page_login(self, page_login):
        self.page_login = page_login

    @property
    def get_product_information(self):
        return self.product_information

    def set_product_information(self, product_information):
        self.product_information = product_information

    @property
    def get_product_id(self):
        return self.product_id

    def set_product_id(self, product_id):
        self.product_id = product_id

    @property
    def get_parent_product(self):
        return self.parent_product

    def set_parent_product(self, parent_product):
        self.parent_product = parent_product

    @property
    def get_adjudication(self):
        return self.adjudication

    def set_adjudication(self, adjudication):
        self.adjudication = adjudication

    @property
    def get_product_positioning(self):
        return self.product_positioning

    def set_product_positioning(self, product_positioning):
        self.product_positioning = product_positioning

    @property
    def get_product_grouping(self):
        return self.product_grouping

    def set_product_grouping(self, product_grouping):
        self.product_grouping = product_grouping

    @property
    def get_fulfillment(self):
        return self.fulfillment

    def set_fulfillment(self, fulfillment):
        self.fulfillment = fulfillment

    @property
    def get_product_application_step(self):
        return self.product_application_step

    def set_product_application_step(self, product_application_step):
        self.product_application_step = product_application_step

    @property
    def get_personal_details(self):
        return self.personal_details

    def set_personal_details(self, personal_details):
        self.personal_details = personal_details

    @property
    def get_summary(self):
        return self.summary

    def set_summary(self, summary):
        self.summary = summary

    @property
    def get_confirmation(self):
        return self.confirmation

    def set_confirmation(self, confirmation):
        self.confirmation = confirmation

    @property
    def get_product_recommendation(self):
        return self.product_recommendation

    def set_product_recommendation(self, product_recommendation):
        self.product_recommendation = product_recommendation

    @property
    def get_terms_and_condition(self):
        return self.terms_and_condition

    def set_terms_and_condition(self, terms_and_condition):
        self.terms_and_condition = terms_and_condition

    @property
    def get_is_paperless(self):
        return self.is_paperless

    def set_is_paperless(self, is_paperless):
        self.is_paperless = is_paperless

    @property
    def get_login_event(self):
        return self.login_event

    def set_login_event(self, login_event):
        self.login_event = login_event

    @property
    def get_user_id(self):
        return self.user_id

    def set_user_id(self, user_id):
        self.user_id = user_id

    @property
    def get_user_auth_state(self):
        return self.user_auth_state

    def set_user_auth_state(self, user_auth_state):
        self.user_auth_state = user_auth_state

    @property
    def get_user_type(self):
        return self.user_type

    def set_user_type(self, user_type):
        self.user_type = user_type

    @property
    def get_error_message(self):
        return self.error_message

    def set_error_message(self, error_message):
        self.error_message = error_message

    @property
    def get_error_type(self):
        return self.error_type

    def set_error_type(self, error_type):
        self.error_type = error_type

    @property
    def get_error_sub_type(self):
        return self.error_sub_type

    def set_error_sub_type(self, error_sub_type):
        self.error_sub_type = error_sub_type

    @property
    def get_error_field(self):
        return self.error_field

    def set_error_field(self, error_field):
        self.error_field = error_field

    @property
    def get_error_code(self):
        return self.error_code

    def set_error_code(self, error_code):
        self.error_code = error_code

    @property
    def get_event_error(self):
        return self.event_error

    def set_event_error(self, event_error):
        self.event_error = event_error

    @property
    def get_advertising(self):
        return self.advertising

    def set_advertising(self, advertising):
        self.advertising = advertising

    @property
    def get_is_login(self):
        return self.is_login

    def set_is_login(self, is_login):
        self.is_login = is_login

    @property
    def get_is_otvc(self):
        return self.is_otvc

    def set_is_otvc(self, is_otvc):
        self.is_otvc = is_otvc

    @property
    def get_is_joint(self):
        return self.is_joint

    def set_is_joint(self, is_joint):
        self.is_joint = is_joint

    @property
    def get_is_otvc_prompt_steps(self):
        return self.is_otvc_prompt_steps

    def set_is_otvc_prompt_steps(self, is_otvc_prompt_steps):
        self.is_otvc_prompt_steps = is_otvc_prompt_steps

    @property
    def get_is_otvc_success_steps(self):
        return self.is_otvc_success_steps

    def set_is_otvc_success_steps(self, is_otvc_success_steps):
        self.is_otvc_success_steps = is_otvc_success_steps

    @property
    def get_events_advertising(self):
        return self.events_advertising

    def set_events_advertising(self, events_advertising):
        self.events_advertising = events_advertising

    @property
    def get_events_ad_click(self):
        return self.events_ad_click

    def set_events_ad_click(self, events_ad_click):
        self.events_ad_click = events_ad_click

    @property
    def get_advertising_tracking_code(self):
        return self.advertising_tracking_code

    def set_advertising_tracking_code(self, advertising_tracking_code):
        self.advertising_tracking_code = advertising_tracking_code

    @property
    def get_advertising_location(self):
        return self.advertising_location

    def set_advertising_location(self, advertising_location):
        self.advertising_location = advertising_location

    @property
    def get_advertising_type(self):
        return self.advertising_type

    def set_advertising_type(self, advertising_type):
        self.advertising_type = advertising_type

