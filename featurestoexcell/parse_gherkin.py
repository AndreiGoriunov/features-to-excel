import re
from os import path
from typing import Callable

from gherkin.parser import Parser

import featurestoexcell.config as config
from featurestoexcell.helpers import parse_validation_steps_file


class ParseGherkin:
    """
    Class to parse and extract information from Gherkin files.

    Attributes:
    - feature: The parsed feature data from the Gherkin file.
    - scenarios: List of scenarios parsed from the Gherkin file.
    - extraction_map: Dictionary mapping desired extraction labels to corresponding methods.
    - output: List containing the extracted information based on extraction_map.
    """

    def __init__(self, file_path: str) -> None:
        """Initialize the ParseGherkin instance with a given Gherkin file."""
        self.feature: dict = self.read_gherkin_file(file_path).get("feature", {})  # type: ignore
        self.scenarios: list = self._get_scenarios()
        self.extraction_map: dict[str, Callable] = {
            "Feature Tags": self._get_feature_tags,
            "Scenario Tags": self._get_scenario_tags,
            "Scenario Name": self._get_scenario_name,
            "Validation Steps": self._get_validation_steps,
            "Feature Name": self._get_feature_name,
        }
        self.output: list[list] = []

    def read_gherkin_file(self, file_path: str):
        """Read and parse a Gherkin file given its file path."""
        with open(file_path, "r") as f:
            gherkin_document = Parser().parse(f.read())
        return gherkin_document

    def get_info_from_gherkin_file(self, extraction_info: list[str]) -> list[list[str]]:
        """
        Extract the desired information from the Gherkin file based on the provided extraction_info list.

        Args:
        - extraction_info: List of labels indicating which information to extract.

        Returns:
        - A list of lists containing the extracted information.
        """
        output: list[list[str]] = []
        for scenario in self.scenarios:
            self.scenario = scenario
            row: list[str] = []
            for info in extraction_info:
                if info in self.extraction_map.keys():
                    row.append(self.extraction_map[info]())
            output.append(row)
        return output

    def _get_scenarios(self) -> list:
        """Extract and return the scenarios from the parsed Gherkin feature."""
        children = self.feature.get("children", [])
        scenarios = []
        for child in children:
            scenario = child.get("scenario", None)
            if scenario:
                scenarios.append(scenario)
        return scenarios

    def _get_feature_name(self) -> str:
        """Extract and return the feature's name."""
        return str(self.feature.get("name"))

    def _get_feature_tags(self) -> str:
        """Extract and return the feature's tags as a string."""
        return " ".join([tag["name"] for tag in self.feature.get("tags", [])])

    def _get_scenario_tags(self) -> str:
        """Extract and return the current scenario's tags as a string."""
        scenario_tags = [tag["name"] for tag in self.scenario.get("tags", [])]
        return " ".join(scenario_tags)

    def _get_scenario_name(self) -> str:
        """Extract and return the name of the current scenario."""
        return self.scenario["name"]

    def _get_steps_from_scenario(self) -> list:
        """Return a list of steps from the current scenario."""
        steps_list = []
        for step in self.scenario["steps"]:
            steps_list.append(step["text"])
        return steps_list

    def _get_validation_steps(self) -> str:
        """
        Extract validation steps from the current scenario. The extraction is based on a regex pattern defined
        in a config file.

        Returns:
        - A string containing the matched validation steps.
        """
        # Check properties and get the regex file
        validation_steps_rel_filepath = config.PROPERTIES.get(
            "validation-steps-filepath"
        )
        if not validation_steps_rel_filepath:
            return "No validation steps file found. Check config.properties"

        validation_steps_abs_filepath: str = path.normpath(
            path.join(config.SCRIPT_DIR, validation_steps_rel_filepath)
        )
        validation_steps_regex: str = parse_validation_steps_file(
            validation_steps_abs_filepath
        )

        validation_steps: str = self._extract_validation_steps(validation_steps_regex)

        return validation_steps

    def _extract_validation_steps(self, regex: str) -> str:
        """
        Extract steps from the current scenario based on a given regex pattern.

        Args:
        - regex: The regex pattern to match against the steps.

        Returns:
        - A string containing the matched steps.
        """
        steps: list[str] = self._get_steps_from_scenario()
        matched_steps = [step for step in steps if re.search(regex, step)]
        return "\n".join(matched_steps)
