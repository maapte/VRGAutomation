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
        self.interaction_tool_name = ""
        self.interactive_tool_complete = ""
        self.interactive_tool_start = ""
