from routing.router import Route, debug_logging
#from anvil.js.window import navigator

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
