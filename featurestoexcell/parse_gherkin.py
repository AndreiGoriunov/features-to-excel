import os

from . import config
from gherkin.parser import Parser


def parse_gherkin_file(file_path: str):
    with open(file_path, "r") as f:
        gherkin_document = Parser().parse(f.read())
    return gherkin_document


def extract_tags(parsed_document):
    feature = parsed_document.get("feature", {})
    feature_tags = [tag["name"] for tag in feature.get("tags", [])]

    scenario_tags = {}
    for scenario in feature.get("children", []):
        if "scenario" in scenario:
            scenario_name = scenario["scenario"]["name"]
            scenario_tags[scenario_name] = [
                tag["name"] for tag in scenario["scenario"].get("tags", [])
            ]

    return feature_tags, scenario_tags


def get_list_of_feature_paths(dir_path) -> list[str]:
    """
    Walks the directory, putting all feature files into a list.

    :param dir_path: The directory to start walking from.
    """
    feature_paths = []
    for root, _, files in os.walk(dir_path):
        for name in files:
            _path = os.path.join(root, name)
            if _path.lower().endswith(".feature"):
                feature_paths.append(_path)
    return [path.replace(config.FEATURE_DIR, "").lstrip(os.sep) for path in feature_paths]


def run():
    features_paths: list[str] = get_list_of_feature_paths(config.FEATURE_DIR)
    for _path in features_paths:
        gherkin_path = os.path.join(config.FEATURE_DIR, _path)
        parsed_document = parse_gherkin_file(gherkin_path)

        feature_tags, scenario_tags = extract_tags(parsed_document)

        print("Feature Tags:", feature_tags)
        for scenario, tags in scenario_tags.items():
            print(f"Tags for Scenario '{scenario}':", tags)
