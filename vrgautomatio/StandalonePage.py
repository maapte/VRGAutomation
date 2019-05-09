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
        self.errors_type = ""
        self.errors_sub_type = ""
        self.errors_field = ""
        self.errors_code = ""

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
    def get_route_name(self):
         return self.page_name

    def set_route_name(self, route_name):
        self.routeName = route_name

    @property
    def get_page_path(self):
         return self.page_path

    def set_page_path(self, page_path):
        self.page_path = page_path

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

    def set_UserType(self, user_type):
        self.user_type = user_type


    @property
    def get_error_code(self):
         return self.error_code

    def set_error_code(self, error_code):
        self.error_code = error_code
