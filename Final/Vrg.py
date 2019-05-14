"""
__author__ : Manish Apte
__maintainer__ : Manish Apte
__organization__ : Deloitte
"""


class Vrg:

    def __init__(self):
        self.project_name = ""
        self.user_name = ""
        self.mobile_json = "true"
        self.test_case = "true"
        self.application_type = ""
        self.site_name = ""
        self.site_brand = ""
        self.site_type = ""
        self.site_environment = "{production | development}"
        self.site_app_version = "{dynamic}"
        self.site_last_build_date = "{dynamic}"
        self.pages = list()
        self.forms = list()
        self.interaction = list()
        self.download = list()

    @property
    def get_project_name(self):
        return self.project_name

    def set_project_name(self, project_name):
        self.project_name = project_name

    @property
    def get_user_name(self):
        return self.user_name

    def set_user_name(self, user_name):
        self.user_name = user_name

    @property
    def get_site_name(self):
        return self.site_name

    def set_site_name(self, site_name):
        self.site_name = site_name

    @property
    def get_site_brand(self):
        return self.site_brand

    def set_site_brand(self, site_brand):
        self.site_brand = site_brand

    @property
    def get_site_type(self):
        return self.site_type

    def set_site_type(self, site_type):
        self.site_type = site_type

    @property
    def get_application_type(self):
        return self.application_type

    def set_application_types(self, application_type):
        self.application_type = application_type

    @property
    def get_site_environment(self):
        return self.site_environment

    def set_site_environment(self, site_environment):
        self.site_environment = site_environment

    @property
    def get_site_app_version(self):
        return self.site_app_version

    def set_site_app_version(self, site_app_version):
        self.site_app_version = site_app_version

    @property
    def get_site_last_build_date(self):
        return self.site_last_build_date

    def set_site_last_build_date(self, site_last_build_date):
        self.site_last_build_date = site_last_build_date

    @property
    def get_mobile_json(self):
        return self.mobile_json

    def set_mobile_json(self, mobile_json):
        self.mobile_json = mobile_json

    @property
    def get_test_case(self):
        return self.test_case

    def set_test_case(self, test_case):
        self.test_case = test_case
