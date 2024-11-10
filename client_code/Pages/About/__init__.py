from ._anvil_designer import AboutTemplate
from anvil import *


class About(AboutTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

    def heading_1_show(self, **event_args):
        """This method is called when the component is shown on the screen."""
        pass

    def button_1_click(self, **event_args):
        """This method is called when the component is clicked."""
        pass
