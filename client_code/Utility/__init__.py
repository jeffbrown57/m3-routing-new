from ._anvil_designer import UtilityTemplate
from anvil import *
import anvil.server



class Utility(UtilityTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

    def button_1_click(self, **event_args):
        """This method is called when the component is clicked."""
        alert("Help Me ?",  title="Educ Summary", large=False, buttons=[Button(text="Click Me")])
        pass
