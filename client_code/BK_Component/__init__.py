from ._anvil_designer import BK_ComponentTemplate
from anvil import *


class BK_Component(BK_ComponentTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

    def button_1_click(self, **event_args):
        """This method is called when the component is clicked."""
        Notification("You have submitted debor credentials", title="BK Case").show()
        pass
