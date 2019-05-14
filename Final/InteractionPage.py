"""
__author__ : Manish Apte
__maintainer__ : Manish Apte
__organization__ : Deloitte
"""


class InteractionPage:
    """" Interaction Page class handle interaction attributes"""
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
        self.site_interaction_event = "true"
        self.interaction_name = ""

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
    def get_site_interaction_event(self):
        return self.site_interaction_event

    def set_site_interaction_event(self,site_interaction_event):
        self.site_interaction_event = site_interaction_event

    @property
    def get_interaction_name(self):
        return self.interaction_name;

    def set_interaction_name(self,interaction_name):
        self.interaction_name = interaction_name
