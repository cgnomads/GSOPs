import hou

import os
import json
import inspect
import webbrowser

from pathlib import Path
from datetime import datetime


GSOPS_BASE_PATH = hou.getenv("GSOPS") or str(Path(inspect.getfile(inspect.currentframe())).parent.parent)
POPUP_INFO_FILE = os.path.join(GSOPS_BASE_PATH, "info", "popup_init.json")
GSOPS_STATE_DIR = os.path.join(GSOPS_BASE_PATH, ".gsops_state")
POPUP_STATE_FILE = os.path.join(GSOPS_STATE_DIR, "popup_init.json")

DATE_FORMAT = "%Y-%m-%d"


def ensure_state_dir():
    os.makedirs(GSOPS_STATE_DIR, exist_ok=True)


def load_json(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    return {}


def save_json(file_path, data):
    ensure_state_dir()
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)


def parse_date(date_str):
    try:
        return datetime.strptime(date_str, DATE_FORMAT) if date_str else None
    except ValueError:
        return None  # Fallback if the date format is incorrect


def should_show_popup():
    state = load_json(POPUP_STATE_FILE)
    popup_data = load_json(POPUP_INFO_FILE)

    popup_date = parse_date(popup_data.get("date"))
    state_date = parse_date(state.get("last_seen_date"))

    # Show popup if state_date is newer than popup_date or if no state exists
    if not state_date or (popup_date and popup_date > state_date):
        state["last_seen_date"] = popup_data.get("date")
        save_json(POPUP_STATE_FILE, state)
        return popup_data.get("popup")

    return None


def show_delayed_popup():
    popup = should_show_popup()
    if not popup:
        hou.ui.removeEventLoopCallback(show_delayed_popup)
        return

    buttons = popup.get("buttons", [])
    button_labels = [b["text"] for b in buttons]
    actions = {b["text"]: b for b in buttons}

    selected_index = hou.ui.displayMessage(
        popup["content"],
        title=popup["title"],
        buttons=button_labels
    )

    if 0 <= selected_index < len(button_labels):
        button = actions[button_labels[selected_index]]
        if button.get("action") == "open_url":
            webbrowser.open(button.get("url"))

    hou.ui.removeEventLoopCallback(show_delayed_popup)


if hou.isUIAvailable():
    hou.ui.addEventLoopCallback(show_delayed_popup)