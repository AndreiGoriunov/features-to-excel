import PySimpleGUI as sg
from .window_config import *
from .thread_handlers import feature_to_excel_handler

class GUI:
    def __init__(self) -> None:
        self.current_window: str = HOME
        self.location: tuple | None = None
        self._create_new_window()
        self._main_loop()

    def _create_new_window(self):
        window_details: dict = LAYOUT_CONFIG.get(self.current_window, {})
        title: str = window_details.get("title", "")
        layout: str = window_details.get("layout", [])()

        # Create the window without specifying the location
        if self.location:
            new_window = sg.Window(
                title, layout, icon=ICON, location=self.location
            )
        else:
            new_window = sg.Window(title, layout, icon=ICON)

        self.window: sg.Window = new_window

    def _main_loop(self):
        while True:
            event, values = self.window.read()
            if not event == sg.WINDOW_CLOSED:
                self.location = self.window.CurrentLocation()
            # Handle the events
            if event == "Convert":
                feature_to_excel_handler(self.window, values)
            elif event in LAYOUT_CONFIG:
                self.window.close()
                self.current_window = event
                self._create_new_window()
            elif event == sg.WINDOW_CLOSED:
                self.window.close()
                break
            else:
                pass