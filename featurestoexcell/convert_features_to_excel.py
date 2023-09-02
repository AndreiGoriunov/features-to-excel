from os import sep

import featurestoexcell.config as config
from featurestoexcell.helpers import (
    combine_dicts,
    generate_sheet_name,
    get_dir_path_elements,
)
from featurestoexcell.utils import (
    ExcelWriter,
    get_list_of_file_paths,
    str_list_to_py_list,
)

def convert_features_to_excel(feature_dir: str, output_dir: str):
    HEADERS: list = str_list_to_py_list(config.PROPERTIES["data-headers"])
    feature_dir_struct: str = config.PROPERTIES["feature-directory-structure"]
    excel_sheet_format: str = config.PROPERTIES["excel-sheet-format"]
    parsed_feature_dir_struct: dict[int, str] = get_dir_path_elements(
        feature_dir_struct
    )
    # TODO Temporary
    feature_dir = "C:/Users/aagor/Downloads/features"  # OVERWRITE
    output_dir = "C:/Users/aagor/Downloads/output"  # OVERWRITE

    feature_paths: list[str] = get_list_of_file_paths(feature_dir)

    ew = ExcelWriter(output_dir)

    for path_ in feature_paths:
        relative_path: str = path_.replace(feature_dir, "").lstrip(sep)
        parsed_path: dict[int, str] = get_dir_path_elements(relative_path)
        combined_dict: dict[str, str] = combine_dicts(
            parsed_feature_dir_struct, parsed_path
        )
        sheet_name: str = generate_sheet_name(excel_sheet_format, combined_dict)

        # TODO Parse Gherkin here and get a list of values based on HEADERS
        values = [combined_dict["."], "@tags", "scenario desc", "my validation"]
        ew.write_to_worksheet(sheet_name, HEADERS, values)

    ew.save_workbook("test")
