import json
import time
from pathlib import Path

import hou

GSOPS_PATH = Path(hou.text.expandString("$GSOPS"))
GSOPS_CONFIG_FILE_PATH = GSOPS_PATH / ".gsops/config.json"
GSOPS_CONFIG_FILE_UPDATE_MARKER_PATH = GSOPS_PATH / ".gsops/.config_json_touched"
GSPLAT_CONFIG_INCLUDE_DIR = GSOPS_PATH / "plugin/include"


def load_settings():
    config_file = Path(GSOPS_CONFIG_FILE_PATH)
    if not config_file.exists():
        return {}
    with open(config_file, "r") as f:
        config_file_dict = json.load(f)
    return config_file_dict.get("plugin_settings", {})


def save_settings(settings_dict):
    config_file = Path(GSOPS_CONFIG_FILE_PATH)
    config_file.parent.mkdir(parents=True, exist_ok=True)
    if config_file.exists():
        with open(config_file, "r") as f:
            try:
                config_file_dict = json.load(f)
            except json.JSONDecodeError:
                config_file_dict = {}
    else:
        config_file_dict = {}
    # Update only the plugin_settings section
    config_file_dict["plugin_settings"] = settings_dict
    with open(config_file, "w") as f:
        json.dump(config_file_dict, f, indent=4)

def apply_settings():
    # Updating this file is what makes the C++ plugin realize it needs to update settings.
    # It's not great but it avoids inlinecpp
    GSOPS_CONFIG_FILE_UPDATE_MARKER_PATH.write_text(str(int(time.time())) + "\n")
