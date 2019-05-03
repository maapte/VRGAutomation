class StandalonePage:

    #All member variables and methods are public by default in Python. So when you want to make your member public, you just do nothing.
    def __init__(self):

        #Page Level Variables
        self.pageName = ''
        self.pageReferrer = "{dynamic}"
        self.pageLanguage = "{en|fr}"
        self.pageView = "true"
        self.pageAccessibilty = "true"
        self.pagePath = ''
        self.pageUrl = "{dynamic}"
        self.pageReferrer="{dynamic}"
        self.pageLogin = "true"
        self.pageHierarchy="{dynamic}"
        # user level variables
        self.loginEvent = ""
        self.userId = ""
        self.userType = ""
        self.userAuthState = ""


        #Error Lever variables
        self.eventError = "false"
        self.errorMessage=""
        self.errorsType = ""
        self.errorsSubType = ""
        self.errorsField = ""
        self.errorsCode = ""

     #getter for Class Memeber
    @property
    def get_PageName(self):
         return self.pageName

    def set_pageName(self,pageName):
        self.pageName = pageName

    @property
    def get_PageReferrer(self):
         return self.pageReferrer

    def set_PageReferrer(self,pageReferrer):
        self.pageReferrer = pageReferrer

    @property
    def get_RouteName(self):
         return self.pageName

    def set_RouteName(self,routeName):
        self.routeName = routeName

    @property
    def get_PagePath(self):
         return self.pagePath

    def set_pagePath(self,pagePath):
        self.pagePath = pagePath

    @property
    def get_UserId(self):
         return self.userId

    def set_UserId(self,userId):
        self.userId = userId

    @property
    def get_UserAuthState(self):
         return self.userAuthState

    def set_UserAuthState(self,userAuthState):
        self.userAuthState = userAuthState

    @property
    def get_UserType(self):
         return self.userType

    def set_UserType(self,userType):
        self.userType = userType


    @property
    def get_ErrorCode(self):
         return self.errorCode

    def set_ErrorCode(self,errorCode):
        self.errorCode = errorCode
