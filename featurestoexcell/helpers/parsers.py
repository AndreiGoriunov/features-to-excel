import re

def get_dir_path_elements(directory_path:str) -> dict[int, str]:
    """
    Parse the given directory path to capture each element and its position.

    Args:
    - directory_path (str): The directory path string to parse.

    Returns:
    - dict[int, str]: A dictionary mapping each element's position to its name.

    Example:
    >>> parse_directory_structure("type\\service\\.")
    {0: 'type', 1: 'service', 2: '.'}
    """
    elements = re.split(r"[/\\]", directory_path)
    return {index: elem for index, elem in enumerate(elements)}

def combine_dicts(config_dict: dict[int, str], feature_path_dict:dict[int, str]) -> dict[str, str]:
    """
    Combine two dictionaries based on the structure defined in config_dict and the values in feature_path_dict.

    Args:
    - config_dict (dict[int, str]): A dictionary defining the structure of keys.
    - feature_path_dict (dict[int, str]): A dictionary containing the actual values.

    Returns:
    - dict[str, str]: A combined dictionary with keys from config_dict and values from feature_path_dict.

    Example:
    >>> combine_dicts({0: 'type', 1: 'service', 2: '.'}, {0: "api", 1: "products", 2: "http", 3: "feature.name"})
    {'type': 'api', 'service': 'products', '.': 'http/feature.name'}
    """
    result:dict[str, str] = {config_dict[key]: feature_path_dict.get(key, '') for key in config_dict}
    # Making sure the '.' key combines the rest of the path
    dot_index = list(config_dict.values()).index('.')
    if dot_index in feature_path_dict:
        result['.'] = '/'.join([value for key, value in feature_path_dict.items() if key >= dot_index])
    return result

def generate_sheet_name(format_string: str, combined_dict: dict[str, str]) -> str:
    """
    Generate a sheet name using the format string and values from the combined dictionary.

    Args:
    - format_string (str): The format string indicating placeholders for keys.
    - combined_dict (dict[str, str]): A dictionary with keys and their respective values.

    Returns:
    - str: The generated sheet name.

    Example:
    >>> generate_sheet_name("type-service", {'type': 'api', 'service': 'products', '.': 'feature.name'})
    'api-products'
    """
    for key, value in combined_dict.items():
        format_string = format_string.replace(key, value)
    return format_string