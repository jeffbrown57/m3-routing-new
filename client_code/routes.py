from routing.router import Route, debug_logging

debug_logging(True)

class Home(Route):
    path = "/"
    form = "Pages.Home"

class About(Route):
    path = "/about"
    form = "Pages.About"
