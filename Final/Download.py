"""
__author__ : Manish Apte
__maintainer__ : Manish Apte
__organization__ : Deloitte
"""


class Download:
    """" Download Page class handle Download attributes"""
    def __init__(self):
        self.page_name = "{dynamic}"
        self.page_referrer = "{dynamic}"
        self.page_language = "{dynamic}"
        self.page_view = "false"
        self.page_accessibility = "{dynamic}"
        self.page_path = "{dynamic}"
        self.page_url = "{dynamic}"
        self.page_login = "{dynamic}"
        self.page_hierarchy = "{dynamic}"
        self.user_id = ""
        self.user_type = ""
        self.user_auth_state = ""
        self.events_download = "true"
        self.download_file_name = ""
        self.download_file_type = ""
        self.event_error = ""
        self.error_message = ""
        self.error_type = ""
        self.error_sub_type = ""
        self.error_field = ""
        self.error_code = ""

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
    def get_events_download(self):
        return self.events_download

    def set_events_download(self, events_download):
        self.events_download = events_download

    @property
    def get_download_file_name(self):
        return self.download_file_name

    def set_download_file_name(self, download_file_name):
        self.download_file_name = download_file_name

    @property
    def get_download_file_type(self):
        return self.download_file_type

    def set_download_file_type(self, download_file_type):
        self.download_file_type = download_file_type
