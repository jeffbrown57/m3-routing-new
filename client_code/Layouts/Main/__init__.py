from ._anvil_designer import MainTemplate
from anvil import *


class Main(MainTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

    def nav_link_1_click(self, **event_args):
        """This method is called when the component is clicked"""
        pass

    def utility_1_degree(self, received, **event_args):
        """This method is called Degree Obtained"""
        Notification("cust_comp_reached").show()
        pass

   