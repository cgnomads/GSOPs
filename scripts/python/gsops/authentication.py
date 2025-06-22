import hou
import inspect
import json
import requests
from pathlib import Path

GSOPS_PATH = hou.text.expandString("$GSOPS") or str(Path(inspect.getfile(inspect.currentframe())).parent.parent)
GSOPS_LICENSE_FILE_PATH = f"{GSOPS_PATH}/.gsops/license"
GSOPS_CONFIG_FILE_PATH = f"{GSOPS_PATH}/.gsops/config.json"
GSOPS_WEBHOOK_URL = "https://flask-api-366260406836.us-central1.run.app/gsops-webhook"


def retrieve_installed_license_details():
    license_file_path = Path(GSOPS_LICENSE_FILE_PATH)
    if not license_file_path.exists():
        return "", ""    
    try:
        with open(license_file_path, "r") as f:
            tokens = f.readline().strip().split()
            if len(tokens) == 2:
                email = tokens[0]
                license_key = tokens[1]
                return email, license_key
    except Exception as e:
        return "", ""
        

def save_license_details(email, license_key):
    license_file_path = Path(GSOPS_LICENSE_FILE_PATH)
    license_file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(license_file_path, "w") as f:
        f.write(f"{email} {license_key}\n")


def authentication_level():
    if hasattr(hou.session, "gsops") and "auth_level" in hou.session.gsops:
        return hou.session.gsops["auth_level"]
    return 0

def authenticate():
    # Return cached auth_level if already set
    current_auth_level = authentication_level()
    if current_auth_level > 0:
        return current_auth_level

    license_file_path = Path(GSOPS_LICENSE_FILE_PATH)
    if not license_file_path.exists():
        return 0

    email, key = retrieve_installed_license_details()
    # print(f"GSOPs Houdini session autentication for user \"{email}\"")

    try:
        response = requests.post(
            GSOPS_WEBHOOK_URL,
            json={"email": email, "key": key},
            timeout=5
        )
        response.raise_for_status()  # Raises HTTPError if not 2xx
        data = response.json()

        auth_level = 1 if data.get("success") else 0
        if auth_level > 0:
            if not hasattr(hou.session, "gsops"):
                hou.session.gsops = {}
            hou.session.gsops["auth_level"] = auth_level
            # print("GSOPs Houdini session authentication success.")
            return auth_level
        # else:
        #     print(f"Authentication failed: {data.get('error', 'Unknown error')}")
    except requests.exceptions.HTTPError as e:
        pass
        # print(f"Could not authenticate. HTTP error: {e.response.status_code}")
    except requests.exceptions.RequestException as e:
        pass
        # print(f"Could not authenticate. Network error: {e}")
    except Exception as e:
        pass
        # print(f"Could not authenticate. Unexpected error: {str(e)}")
    return 0


def setup_for_authentication_level(level=0):
    # Currently, this funtion only does OTL visibility, but we might add more stuff later.

    # Unhide everything...
    all_node_type_categories = hou.nodeTypeCategories().keys()
    for node_type_category in all_node_type_categories:
        node_category = hou.nodeTypeCategories().get(node_type_category) 
        for node_type_name, node_type in node_category.nodeTypes().items():
            if not node_type_name.startswith("gsop::"):
                continue
            node_type.setHidden(False)

    # And now retrieve config to determine visibility of nodes.
    config_file = Path(GSOPS_CONFIG_FILE_PATH)
    if not config_file.exists():
        return
    with open(config_file, "r") as f:
        config_file_dict = json.load(f)
    level_str = str(level)
    ophide_levels = config_file_dict.get("ophide_levels", {})
    otl_hide_dict = ophide_levels.get(level_str)
    if not otl_hide_dict:
        return
            
    # And hide nodes that are not available at this authentication level...
    for node_type_category, node_type_names in otl_hide_dict.items():
        if node_type_category not in all_node_type_categories:
            continue
        node_type_patterns = [f"*{name}*" for name in node_type_names]
        node_category = hou.nodeTypeCategories().get(node_type_category)
        if not node_category:
            continue
        for node_type_name, node_type in node_category.nodeTypes().items():
            if not node_type_name.startswith("gsop::"):
                continue
            should_be_visible = (
                not any(hou.text.patternMatch(pattern, node_type_name) for pattern in node_type_patterns)
            )
            node_type.setHidden(not should_be_visible)


def authenticate_and_setup():
    auth_level = authenticate()
    setup_for_authentication_level(auth_level)
    return auth_level
