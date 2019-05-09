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
        self.event_error = "false"
        self.error_message = ""
        self.error_type = ""
        self.errors_sub_type = ""
        self.errors_field = ""
        self.errors_code = ""
