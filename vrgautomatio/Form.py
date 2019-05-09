class Form:

    def __init__(self):
        self.form_name = ''
        self.no_of_steps = ''
        self.is_product_exist = ''
        self.is_transaction_exist = ''
        self.steps = list()

    @property
    def get_form_name(self):
        return self.form_name

    def set_form_name(self, form_name):
        self.form_name = form_name

    @property
    def get_no_of_steps(self):
        return self.no_of_steps

    def set_no_of_steps(self, no_of_steps):
        self.no_of_steps = no_of_steps

    @property
    def get_is_product_exist(self):
        return self.is_product_exist

    def set_is_product_exist(self, is_product_exist):
        self.is_product_exist = is_product_exist

    @property
    def get_is_transaction_exist(self):
        return self.is_transaction_exist

    def set_is_transaction_exist(self, is_transaction_exist):
        self.is_transaction_exist = is_transaction_exist
