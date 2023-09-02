from os import path, makedirs

from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.worksheet import Worksheet

from featurestoexcell.utils import get_datetime


class ExcelWriter:
    def __init__(self, output_dir: str, default_column_width: int = 40) -> None:
        self.output_dir = path.normpath(output_dir)
        self.default_column_width = default_column_width
        self.wb = Workbook()
        self.wb.active.title = "Summary"  # type: ignore

    def _set_default_column_width(self, ws: Worksheet, headers):
        for i in range(
            1, len(headers) + 1
        ):  # +1 because range is exclusive on the upper limit
            col_letter = get_column_letter(i)
            ws.column_dimensions[col_letter].width = self.default_column_width

    def save_workbook(self, base_name: str):
        # Make sure the output directory exists
        makedirs(self.output_dir, exist_ok=True)

        save_filepath: str = path.normpath(
            path.join(self.output_dir, f"{base_name}_{get_datetime()}.xlsx")
        )
        self.wb.save(save_filepath)

    def write_to_worksheet(self, name: str, headers: list[str], values: list[str]):
        sheet_names = [ws.title for ws in self.wb.worksheets]
        if not name in sheet_names:
            ws: Worksheet = self.wb.create_sheet(name)
            ws.append(headers)
            self._set_default_column_width(ws, headers)
        ws = self.wb[name]
        ws.append(values)
