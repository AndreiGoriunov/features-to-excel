from os import path

from featurestoexcell.utils import parse_properties

SCRIPT_DIR: str = ""
PROPERTIES_PATH = r".\config.properties"
PROPERTIES: dict[str, str] = {}

def set_properties():
    global PROPERTIES
    PROPERTIES = parse_properties(path.join(SCRIPT_DIR, PROPERTIES_PATH))

def set_config(main_script_dir: str):
    global SCRIPT_DIR
    SCRIPT_DIR = main_script_dir
    set_properties()
