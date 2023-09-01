import PySimpleGUI as sg

# Styles
TITLE = "Rei's Feature to Excel"
TITLE_FONT = ("Any", 13, "bold")
BUTTON_FONT = ("Any", 13)
MIN_WIDTH = 50
ICON = "icon.ico"
# Pages
HOME = "Converter"


def home_layout():
    return [
            [sg.Text(HOME, font=TITLE_FONT)],
            [sg.Text("", size=(MIN_WIDTH, 0))],
            [
                sg.Text("Select feature dir:", size=(13, 1)),
                sg.InputText(key="-FOLDER-"),
                sg.FolderBrowse(),
            ],
            [
                sg.Text("Select output dir:", size=(13, 1)),
                sg.InputText(key="-FOLDER-"),
                sg.FolderBrowse(),
            ],
            [
                sg.Button("Convert", key="Convert"),
                sg.Text("", size=(20, 0), key="-FEEDBACK-"),
            ],
        ]

LAYOUT_CONFIG = {
    HOME: {"title": TITLE, "layout": home_layout},
}
