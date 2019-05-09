class VRGObject:

    def __init__(self):
        self.ProjectName = ""
        self.userName = ""
        self.MobileJson = "True"
        self.TestCase = "True"
        self.applicationType = ""
        self.siteName = ""
        self.sitebrand = ""
        self.siteType = ""
        self.siteEnviroment = "{production | development}"
        self.siteAppVersion = "{dynamic}"
        self.siteLastBuildDate = "{dynamic}"
        self.pages = list()
        self.forms = list()
        self.interaction = list()
        self.download = list()

    @property
    def get_ProjectName(self):
        return self.ProjectName

    def set_ProjectName(self, ProjectName):
        self.ProjectName = ProjectName

    @property
    def get_UserName(self):
        return self.userName

    def set_UserName(self, userName):
        self.userName = userName

    @property
    def get_SiteName(self):
        return self.siteName

    def set_SiteName(self, siteName):
        self.siteName = siteName

    @property
    def get_SiteBrand(self):
        return self.sitebrand

    def set_SiteBrand(self, sitebrand):
        self.sitebrand = sitebrand

    @property
    def get_SiteType(self):
        return self.siteType

    def set_SiteType(self, siteType):
        self.siteType = siteType

    @property
    def get_ApplicationType(self):
        return self.applicationType

    def set_ApplicationTypes(self, applicationType):
        self.applicationType = applicationType

    @property
    def get_siteEnviroment(self):
        return self.siteEnviroment

    def set_siteEnviroment(self, siteEnviroment):
        self.siteEnviroment = siteEnviroment

    @property
    def get_siteAppVersion(self):
        return self.siteAppVersion

    def set_siteAppVersion(self, siteAppVersion):
        self.siteAppVersion = siteAppVersion

    @property
    def get_siteLastBuildDate(self):
        return self.siteLastBuildDate

    def set_siteLastBuildDate(self, siteLastBuildDate):
        self.siteLastBuildDate = siteLastBuildDate


    @property
    def get_MobileJson(self):
        return self.MobileJson

    def set_MobileJson(self, MobileJson):
        self.MobileJson = MobileJson

    @property
    def get_TestCase(self):
        return self.TestCase

    def set_TestCase(self, TestCase):
        self.TestCase = TestCase
