from datetime import datetime
from os import path, walk, sep
from ast import literal_eval


def get_datetime(format_: str = "%Y-%m-%d_%H-%M-%S") -> str:
    now = datetime.now()
    date_str: str = now.strftime(format_)
    return date_str


def get_list_of_file_paths(dir_path: str) -> list[str]:
    """
    Walks the directory, putting all feature files into a list.

    :param dir_path: The directory to start walking from.
    """
    feature_paths = []
    for root, _, files in walk(dir_path):
        for name in files:
            _path = path.join(root, name)
            if _path.lower().endswith(".feature"):
                feature_paths.append(_path)
    return feature_paths


def str_list_to_py_list(str_list: str) -> list:
    return literal_eval(str_list)
