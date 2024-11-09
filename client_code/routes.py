import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from routing.router import Route, debug_logging

debug_logging(True)

class Home(Route):
    path = "/"
    form = "Pages.Home"

class About(Route):
    path = "/about"
    form = "Pages.About"

class ContactUS(Route):
    path = "/contact"
    form = "Pages.ContactUS"
