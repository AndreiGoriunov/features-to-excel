from threading import Thread

import PySimpleGUI as sg

import featurestoexcell.config as config
from featurestoexcell.convert_features_to_excel import convert_features_to_excel
from featurestoexcell.gui.window_config import FEATURE_DIR_KEY, OUTPUT_DIR_KEY
from featurestoexcell.helpers import (
    combine_dicts,
    generate_sheet_name,
    get_dir_path_elements,
)


def feature_to_excel_handler(window: sg.Window, values: dict):
    feature_dir = values.get(FEATURE_DIR_KEY)
    output_dir = values.get(OUTPUT_DIR_KEY)
    # Starting the thread and checking it ============================================
    thread = Thread(target=convert_features_to_excel, args=(feature_dir, output_dir))
    window["-FEEDBACK-"].update("Converting... Please wait.")  # type: ignore
    window.refresh()
    thread.start()
    while True:
        event, values = window.read(timeout=100)  # type: ignore ; checks every 100 ms
        if event == sg.WINDOW_CLOSED:
            window.close()
            return
        if not thread.is_alive():  # if the thread has finished its job
            window["-FEEDBACK-"].update("Finished.")  # type: ignore
            break
