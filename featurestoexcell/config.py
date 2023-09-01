from os import path

from featurestoexcell.utils.config_parser import parse_properties

SCRIPT_DIR: str = ""
PROPERTIES_PATH = r".\config.properties"
PROPERTIES: dict[str, str] = {}
FEATURE_DIR = ""

def set_properties():
    global PROPERTIES, FEATURE_DIR
    PROPERTIES = parse_properties(path.join(SCRIPT_DIR, PROPERTIES_PATH))
    FEATURE_DIR = path.join(SCRIPT_DIR, PROPERTIES.get("default-input-directory", ""))

def set_config(main_script_dir: str):
    global SCRIPT_DIR
    SCRIPT_DIR = main_script_dir
    set_properties()
