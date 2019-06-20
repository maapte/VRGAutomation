"""
__author__ : Manish Apte
__maintainer__ : Manish Apte
__organization__ : Deloitte
"""


class StandalonePage:

    def __init__(self):
        self.page_name = ""
        self.page_referrer = "{dynamic}"
        self.page_language = "{en|fr}"
        self.page_view = "true"
        self.page_accessibility = "true"
        self.page_path = ''
        self.page_url = "{dynamic}"
        self.page_login = "true"
        self.page_hierarchy = "{dynamic}"
        self.login_event = ""
        self.user_id = ""
        self.user_type = ""
        self.user_auth_state = ""
        self.event_error = "false"
        self.error_message = ""
        self.error_type = ""
        self.error_sub_type = ""
        self.error_field = ""
        self.error_code = ""
        self.advertising = "false"
        self.events_advertising = ""
        self.events_ad_click = ""
        self.advertising_tracking_code = ""
        self.advertising_location = ""
        self.advertising_type = ""
        self.is_login = ""
        self.is_otvc = "false"
        self.is_otvc_prompt = ""
        self.is_otvc_success = ""


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
    def get_page_login(self):
        return self.page_login

    def set_page_login(self, page_login):
        self.page_login = page_login

    @property
    def get_page_hierarchy(self):
        return self.page_hierarchy

    def set_page_hierarchy(self, page_hierarchy):
        self.page_hierarchy = page_hierarchy

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
    def get_is_otvc_prompt(self):
        return self.is_otvc_prompt

    def set_is_otvc_prompt(self, is_otvc_prompt):
        self.is_otvc_prompt = is_otvc_prompt

    @property
    def get_is_otvc_success(self):
        return self.is_otvc_success

    def set_is_otvc_success(self, is_otvc_success):
        self.is_otvc_success = is_otvc_success
