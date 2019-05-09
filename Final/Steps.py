class Steps:

    def __init__(self):
        self.page_view = "true"
        self.page_path = "{dynamic}"
        self.page_name = ""
        self.page_url = "{dynamic}"
        self.page_referrer = "{dynamic}"
        self.page_hierarchy = "{dynamic}"
        self.page_language = "{en|fr}"
        self.page_referrer = "{dynamic}"
        self.page_accessibility = "true"
        self.step_name = ""
        self.form_step = "true"
        self.form_view = ""
        self.form_submit = ""
        self.form_qualify = ""
        self.page_login = ""
        self.unique_id = "{dynamic}"
        self.transaction_id = "{dynamic}"
        self.transaction_amount = "{dynamic}"
        self.transaction_service_fee = "{dynamic}"
        self.transaction_unit = "{dynamic}"
        self.from_transaction = ""
        self.to_transaction = ""
        self.is_external = ""
        self.is_transaction_complete = ""
        self.product_information = ""
        self.product_id = ""
        self.parent_product = ""
        self.adjudication = ""
        self.product_positioning = ""
        self.product_grouping = ""
        self.fulfillment = ""
        self.product_application_step = ""
        self.personal_details = ""
        self.summary = ""
        self.confirmation = ""
        self.product_recommendation = ""
        self.terms_and_condition = ""
        self.is_paperless = ""
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
    def get_transaction_id(self):
        return self.transaction_id

    def set_transaction_id(self, transaction_id):
        self.transaction_id = transaction_id

    @property
    def get_from_transaction(self):
        return self.from_transaction

    def set_from_transaction(self, from_transaction):
        self.from_transaction = from_transaction

    @property
    def get_to_transaction(self):
        return self.to_transaction

    def set_ToTransaction(self, to_transaction):
        self.to_transaction = to_transaction

    @property
    def get_step_name(self):
        return self.step_name

    def set_step_name(self, step_name):
        self.step_name = step_name

    @property
    def get_form_step(self):
        return self.form_step

    def set_form_step(self, form_step):
        self.form_step = form_step

    @property
    def get_form_steps(self):
        return self.form_steps

    def set_form_steps(self, form_steps):
        self.form_steps = form_steps

    @property
    def get_form_view(self):
        return self.form_view

    def set_form_view(self, form_view):
        self.form_view = form_view

    @property
    def get_form_submit(self):
        return self.form_submit

    def set_form_submit(self, form_submit):
        self.form_submit = form_submit

    @property
    def get_form_qualify(self):
        return self.form_qualify

    def set_form_qualify(self, form_qualify):
        self.form_qualify = form_qualify

    @property
    def get_page_login(self):
        return self.page_login

    def set_page_login(self, page_login):
        self.page_login = page_login

    @property
    def get_product_information(self):
        return self.product_information

    def set_product_information(self, product_information):
        self.product_information = product_information

    @property
    def get_productId(self):
        return self.product_id

    def set_productId(self, productId):
        self.product_id = productId

    @property
    def get_parentProduct(self):
        return self.parent_product

    def set_parentProduct(self, parentProduct):
        self.parent_product = parentProduct

    @property
    def get_adjudication(self):
        return self.adjudication

    def set_adjudication(self, adjudication):
        self.adjudication = adjudication

    @property
    def get_productPositioning(self):
        return self.product_positioning

    def set_productPositioning(self, productPositioning):
        self.product_positioning = productPositioning

    @property
    def get_productGrouping(self):
        return self.product_grouping

    def set_productGrouping(self, productGrouping):
        self.product_grouping = productGrouping

    @property
    def get_fulfillment(self):
        return self.fulfillment

    def set_fulfillment(self, fulfillment):
        self.fulfillment = fulfillment

    @property
    def get_productApplicationStep(self):
        return self.product_application_step

    def set_productApplicationStep(self, productApplicationStep):
        self.product_application_step = productApplicationStep

    @property
    def get_personalDetails(self):
        return self.personal_details

    def set_personalDetails(self, personalDetails):
        self.personal_details = personalDetails

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
    def get_product_recommendation(self):
        return self.product_recommendation

    def set_product_recommendation(self, product_recommendation):
        self.product_recommendation = product_recommendation

    @property
    def get_termsAndCondition(self):
        return self.terms_and_condition

    def set_termsAndCondition(self, termsAndCondition):
        self.terms_and_condition = termsAndCondition

    @property
    def get_isPaperless(self):
        return self.is_paperless

    def set_isPaperless(self, isPaperless):
        self.is_paperless = isPaperless

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
    def get_UserType(self):
        return self.user_type

    def set_user_type(self, user_type):
        self.user_type = user_type
