import os

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


def run(dir_path: str):
    features_paths: list[str] = get_list_of_file_paths(dir_path)
    for _path in features_paths:
        print(_path)
    # for _path in features_paths:
    #     gherkin_path = os.path.join(dir_path, _path)
    #     parsed_document = parse_gherkin_file(gherkin_path)

    #     feature_tags, scenario_tags = extract_tags(parsed_document)

    #     print("Feature Tags:", feature_tags)
    #     for scenario, tags in scenario_tags.items():
    #         print(f"Tags for Scenario '{scenario}':", tags)
