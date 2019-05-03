class StepsPage:

    # All member variables and methods are public by default in Python. So when you want to make your member public, you just do nothing.
    def __init__(self):
        # Page Level Variables
        self.pageView = "true"

        self.pagePath = "{dynamic}"
        self.pageName = ""
        self.pageUrl = "{dynamic}"
        self.pageReferrer="{dynamic}"
        self.pageHierarchy="{dynamic}"
        self.pageLanguage = "{en|fr}"
        self.pageLogin = "true"
        self.pageReferrer = "{dynamic}"
        self.pageAccessibilty="true"

        self.stepName = ''
        self.formStep = 'true'
        self.formView = ''
        self.formsubmit = ''
        self.formQualify = ''
        self.pageLogin = ''
        self.uniqueId='{dynamic}'
        self.eventFormStep='true'

        self.transactionId = '{dynamic}'
        self.transactionamount ='{dynamic}'
        self.transactionServiceFee='{dynamic}'
        self.transactionUnit='{dynamic}'
        self.fromtransaction = ''
        self.totransaction = ''
        self.isExternal = ''
        self.istransactionComplete=''

        self.productInformation = ''
        self.productId = ''
        self.parentProduct = ''
        self.adjudication = ''
        self.productPositioning = ''
        self.productGrouping = ''
        self.fulfillment = ''
        self.productApplicationStep = ''
        self.personalDetails = ''
        self.summary = ''
        self.confirmation = ''
        self.productRecommendation = ''
        self.termsandCondition = ''
        self.isPaperless = ''


        # user level variables
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


    # getter for Class Memeber
    @property
    def get_PageName(self):
        return self.pageName

    def set_pageName(self, pageName):
        self.pageName = pageName

    @property
    def get_TransactionId(self):
        return self.transactionId

    def set_TransactionId(self, transactionId):
        self.transactionId = transactionId

    @property
    def get_FromTransaction(self):
        return self.fromtransaction

    def set_FromTransaction(self, fromtransaction):
        self.fromtransaction = fromtransaction

    @property
    def get_ToTransaction(self):
        return self.fromtransaction

    def set_ToTransaction(self, totransaction):
        self.totransaction = totransaction

    @property
    def get_stepName(self):
        return self.stepName

    def set_stepName(self, stepName):
        self.stepName = stepName

    @property
    def get_formStep(self):
        return self.formStep

    def set_formStep(self, formStep):
        self.formStep = formStep

    @property
    def get_formSteps(self):
        return self.formSteps

    def set_formSteps(self, formSteps):
        self.formSteps = formSteps

    @property
    def get_formView(self):
        return self.formView

    def set_formView(self, formView):
        self.formView = formView

    @property
    def get_formsubmit(self):
        return self.formsubmit

    def set_formsubmit(self, formsubmit):
        self.formsubmit = formsubmit

    @property
    def get_formQualify(self):
        return self.formQualify

    def set_formQualify(self, formQualify):
        self.formQualify = formQualify

    @property
    def get_pageLogin(self):
        return self.pageLogin

    def set_pageLogin(self, pageLogin):
        self.pageLogin = pageLogin

    @property
    def get_productInformation(self):
        return self.productInformation

    def set_productInformation(self, productInformation):
        self.productInformation = productInformation

    @property
    def get_productId(self):
        return self.productId

    def set_productId(self, productId):
        self.productId = productId

    @property
    def get_parentProduct(self):
        return self.parentProduct

    def set_parentProduct(self, parentProduct):
        self.parentProduct = parentProduct

    @property
    def get_adjudication(self):
        return self.adjudication

    def set_adjudication(self, adjudication):
        self.adjudication = adjudication

    @property
    def get_productPositioning(self):
        return self.productPositioning

    def set_productPositioning(self, productPositioning):
        self.productPositioning = productPositioning

    @property
    def get_productGrouping(self):
        return self.productGrouping

    def set_productGrouping(self, productGrouping):
        self.productGrouping = productGrouping

    @property
    def get_fulfillment(self):
        return self.fulfillment

    def set_fulfillment(self, fulfillment):
        self.fulfillment = fulfillment

    @property
    def get_productApplicationStep(self):
        return self.productApplicationStep

    def set_productApplicationStep(self, productApplicationStep):
        self.productApplicationStep = productApplicationStep

    @property
    def get_personalDetails(self):
        return self.personalDetails

    def set_personalDetails(self, personalDetails):
        self.personalDetails = personalDetails

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
    def get_productRecommendation(self):
        return self.productRecommendation

    def set_productRecommendation(self, productRecommendation):
        self.productRecommendation = productRecommendation

    @property
    def get_termsandCondition(self):
        return self.termsandCondition

    def set_termsandCondition(self, termsandCondition):
        self.termsandCondition = termsandCondition

    @property
    def get_isPaperless(self):
        return self.isPaperless

    def set_isPaperless(self, isPaperless):
        self.isPaperless = isPaperless

    @property
    def get_UserId(self):
        return self.userId

    def set_UserId(self, userId):
        self.userId = userId

    @property
    def get_UserAuthState(self):
        return self.userAuthState

    def set_UserAuthState(self, userAuthState):
        self.userAuthState = userAuthState

    @property
    def get_UserType(self):
        return self.userType

    def set_UserType(self, userType):
        self.userType = userType
