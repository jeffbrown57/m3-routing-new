from ._anvil_designer import AboutTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil.js.window import navigator


class About(AboutTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

    def button_to_js_click(self, **event_args):
        """This method is called when the component is clicked."""
        X = "Copy/paste from Anvil is delectable!"
        navigator.clipboard.writeText(X)
        pass

    def button_run_task_click(self, **event_args):
        """This method is called when the component is clicked."""
        ret = anvil.server.call('run_it')
        pass
