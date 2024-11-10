from ._anvil_designer import BK_ComponentTemplate
from anvil import *


class BK_Component(BK_ComponentTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.
    @property
    def case_admin(self):
      print(f"Getting Case-Admin: {self._case_admin}")
      return self._case_admin

    @case_admin.setter
    def case_admin(self, value):
      print(f"Setting case_admin: {value}")
      self._case_admin = value
      #self.column_panel_1.background = value

    def button_1_click(self, **event_args):
        """This method is called when the component is clicked."""
        #print(self.bk_component_1.case_admin()))
        #print(self.case_admin())
        Notification(f"Debtor: {self.text_box_debtor.text}\nChapter: {self.text_box_chapter.text} ", title="BK Case").show()
        pass
