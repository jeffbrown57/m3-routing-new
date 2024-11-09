import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from routing.router import launch
from . import routes  # noqa: F401

if __name__ == "__main__":
    launch()
