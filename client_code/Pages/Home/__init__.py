from ._anvil_designer import HomeTemplate
from anvil import *



class Home(HomeTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)

