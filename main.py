import sys
from os import path

import featurestoexcell.config as config
from featurestoexcell.event_handlers import feature_to_excel_handler
from featurestoexcell.gui import GUI
from featurestoexcell.gui.window_config import HOME, RUN_FEATURESTOEXCEL_KEY


def get_script_dir() -> str:
    if getattr(sys, "frozen", False):
        # The script is running inside a PyInstaller bundle
        print("Running inside a PyInstaller bundle")
        return path.dirname(sys.executable)
    else:
        # The script is running in a normal Python environment
        print("Running from .py file")
        script_path = path.abspath(__file__)
        return path.dirname(script_path)


if __name__ == "__main__":
    config.set_config(get_script_dir())
    app = GUI(HOME)
    app.add_event_handler(RUN_FEATURESTOEXCEL_KEY, feature_to_excel_handler)
    app.start()
