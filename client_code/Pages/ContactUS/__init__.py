from ._anvil_designer import ContactUSTemplate
from anvil import *
from Medicaldash import Utilities_All as utils


class ContactUS(ContactUSTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.
        print(utils.get_author())
        #print(self.bk_component_1.case_admin())
       
        #self.text_box_1.text = utils

    
    