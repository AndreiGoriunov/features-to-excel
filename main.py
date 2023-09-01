import sys
from os import path
from featurestoexcell.gui.gui import GUI
import featurestoexcell.config as config
import featurestoexcell.parse_gherkin as pg

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
    pg.run()
    

    # app = GUI()
