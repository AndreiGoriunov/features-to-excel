from typing import Callable

import PySimpleGUI as sg

from .window_config import *


class GUI:
    """
    GUI class to handle the creation and management of windows using PySimpleGUI.

    Attributes:
        current_window (str): Name of the current window.
        handled_events (dict): Mapping of event names to their handler functions.
        location (tuple, optional): Location of the window. Defaults to None.
    """

    def __init__(self, default_window: str) -> None:
        """Initializes the GUI object, sets the default window, and creates the window."""
        self.current_window: str = default_window
        self.handled_events: dict[str, Callable] = {}
        self.location: tuple | None = None
        self._create_new_window()

    def _create_new_window(self):
        """
        Creates a new window based on the current window's settings.
        If `self.location` is set, it places the window at the specified location.
        """
        window_details: dict = LAYOUT_CONFIG.get(self.current_window, {}) # type: ignore
        title: str = window_details.get("title", "")
        layout: str = window_details.get("layout", [])()

        # Create the window without specifying the location
        if self.location:
            new_window = sg.Window(title, layout, icon=ICON, location=self.location)
        else:
            new_window = sg.Window(title, layout, icon=ICON)

        self.window: sg.Window = new_window

    def add_event_handler(self, key: str, func: Callable):
        """
        Adds an event handler for the specified key.

        Args:
            key (str): The name of the event.
            func (Callable): The function to call when the event is triggered.
        """
        self.handled_events[key] = func

    def start(self):
        """
        Starts the event loop. Handles predefined events, window switches,
        and window closing events.
        """
        while True:
            event, values = self.window.read()  # type: ignore
            if not event == sg.WINDOW_CLOSED:
                self.location = self.window.CurrentLocation()
            # Handle the events
            if event in self.handled_events:
                self.handled_events[event](self.window, values)
            # Handle window switch
            elif event in LAYOUT_CONFIG:
                self.window.close()
                self.current_window = event
                self._create_new_window()
            # Handle window closing
            elif event == sg.WINDOW_CLOSED:
                self.window.close()
                break
