import hou

import os
import json
import requests
import socket
import inspect
import webbrowser

from pathlib import Path
from datetime import datetime



GSOPS_BASE_PATH = hou.getenv("GSOPS") or str(Path(inspect.getfile(inspect.currentframe())).parent.parent)
POPUP_INFO_LOCAL_FILE = os.path.join(GSOPS_BASE_PATH, "misc", "info", "popup_init.json")
POPUP_INFO_REMOTE_FILE = "https://raw.githubusercontent.com/cgnomads/GSOPs/refs/heads/develop/misc/info/popup_init.json"
GSOPS_STATE_DIR = os.path.join(GSOPS_BASE_PATH, ".gsops")
POPUP_STATE_FILE = os.path.join(GSOPS_STATE_DIR, "popup_init.json")
POPUP_STATE_FILE_FALLBACK = os.path.join(os.path.join(GSOPS_BASE_PATH, ".gsops_state"), "popup_init.json")

DATE_FORMAT = "%Y-%m-%d"


def _ensure_state_dir():
    os.makedirs(GSOPS_STATE_DIR, exist_ok=True)


def _save_json(file_path, data):
    _ensure_state_dir()
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

        
def _load_json(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    return {}


def _check_connection(host="8.8.8.8", port=53, timeout=1.0): # Default is Google's DNS server
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error:
        return False


def _fetch_json_from_url(url):
    """Fetch JSON from a GitHub URL if online."""
    if not _check_connection():
        return None
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        # print(f"popup_init : HTTP error occurred: {e}")
        return None
    except requests.exceptions.RequestException as e:
        # print(f"popup_init : Request error occurred: {e}")
        return None
    except ValueError as e:
        # print(f"popup_init : Failed to parse JSON: {e}")
        return None


def _retrieve_popup():
    def _parse_date(date_str):
        try:
            return datetime.strptime(date_str, DATE_FORMAT) if date_str else None
        except ValueError:
            return None
    
    state = _load_json(POPUP_STATE_FILE)
    if not state:
        # try to retrieve state from legacy location
        state = _load_json(POPUP_STATE_FILE_FALLBACK)

    popup_data = None  
    if _check_connection():
        popup_data = _fetch_json_from_url(POPUP_INFO_REMOTE_FILE)
    if not popup_data:    
        popup_data = _load_json(POPUP_INFO_LOCAL_FILE)

    popup_date = _parse_date(popup_data.get("date"))
    state_date = _parse_date(state.get("last_seen_date"))

    # Show popup if state_date is newer than popup_date or if no state exists
    if not state_date or (popup_date and popup_date > state_date):
        state["last_seen_date"] = popup_data.get("date")
        _save_json(POPUP_STATE_FILE, state)
        return popup_data.get("popup")

    return None


def _show_delayed_popup():
    popup = _retrieve_popup()
    if not popup:
        hou.ui.removeEventLoopCallback(_show_delayed_popup)
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

    hou.ui.removeEventLoopCallback(_show_delayed_popup)


def show():
    if hou.isUIAvailable():
        hou.ui.addEventLoopCallback(_show_delayed_popup)
