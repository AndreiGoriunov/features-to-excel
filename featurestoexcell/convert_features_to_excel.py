from os import sep

import featurestoexcell.config as config
from featurestoexcell.helpers import (
    combine_dicts,
    generate_sheet_name,
    get_dir_path_elements,
)
from featurestoexcell.parse_gherkin import ParseGherkin
from featurestoexcell.utils import (
    ExcelWriter,
    get_list_of_file_paths,
    str_list_to_py_list,
)


def convert_features_to_excel(feature_dir: str, output_dir: str):
    """
    Convert Gherkin feature files in a specified directory to an Excel file.

    Args:
    - feature_dir: Directory containing the Gherkin feature files to convert.
    - output_dir: Directory where the generated Excel file should be saved.

    The method uses configurations from 'config.PROPERTIES' to determine:
    - Headers for the Excel sheet.
    - The directory structure of the feature files.
    - The format for naming Excel sheets.
    """
    # Retrieve necessary configurations from properties
    HEADERS: list = str_list_to_py_list(config.PROPERTIES["data-headers"])
    feature_dir_struct: str = config.PROPERTIES["feature-directory-structure"]
    excel_sheet_format: str = config.PROPERTIES["excel-sheet-format"]

    # Parse the provided feature directory structure
    parsed_feature_dir_struct: dict[int, str] = get_dir_path_elements(
        feature_dir_struct
    )

    # Get list of all feature file paths
    feature_paths: list[str] = get_list_of_file_paths(feature_dir)

    # Initialize Excel writer
    ew = ExcelWriter(output_dir)

    # Iterate through each feature file to process and write its data to Excel
    for path_ in feature_paths:
        # Derive the relative path of the feature file by removing the base directory
        relative_path: str = path_.replace(feature_dir, "").lstrip(sep)
        # Parse the derived relative path
        parsed_path: dict[int, str] = get_dir_path_elements(relative_path)
        # Combine parsed directory structure with the parsed path
        combined_dict: dict[str, str] = combine_dicts(
            parsed_feature_dir_struct, parsed_path
        )
        # Generate an appropriate name for the Excel sheet based on the format provided
        sheet_name: str = generate_sheet_name(excel_sheet_format, combined_dict)

        # Parse the Gherkin feature file
        parse_gherkin = ParseGherkin(path_)
        # Extract the necessary rows of data from the Gherkin file based on the headers
        rows: list[list[str]] = parse_gherkin.get_info_from_gherkin_file(HEADERS)
        for row in rows:
            # If the header contains "Feature File", insert the feature file's name in the appropriate position
            if "Feature File" in HEADERS:
                index = HEADERS.index("Feature File")
                row.insert(index, combined_dict["."])
            ew.write_to_worksheet(sheet_name, HEADERS, row)

    # Save the constructed Excel file with the name 'features'
    ew.save_workbook("features")
