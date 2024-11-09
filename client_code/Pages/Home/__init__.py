from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files


class Home(HomeTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)

