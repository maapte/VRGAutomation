class FormsPage:

    #All member variables and methods are public by default in Python. So when you want to make your member public, you just do nothing.
    def __init__(self):

        #Page Level Variables
        self.formName = ''
        self.noOfSteps = ''
        self.flowcatergory = ''
        self.isProductExist = ''
        self.isTransactionExist = ''
        self.steps = list()

    # getter for Class Memeber
    @property
    def get_formName(self):
        return self.formName

    def set_formName(self, formName):
        self.formName = formName

    @property
    def get_noOfSteps(self):
        return self.noOfSteps

    def set_noOfSteps(self, noOfSteps):
        self.noOfSteps = noOfSteps

    @property
    def get_flowcatergory(self):
        return self.flowcatergory

    def set_flowcatergory(self, flowcatergory):
        self.flowcatergory = flowcatergory

    @property
    def get_isProductExist(self):
        return self.isProductExist

    def set_isProductExist(self, isProductExist):
        self.isProductExist = isProductExist

    @property
    def get_isTransactionExist(self):
        return self.isTransactionExist

    def set_isTransactionExist(self, isTransactionExist):
        self.isTransactionExist = isTransactionExist
