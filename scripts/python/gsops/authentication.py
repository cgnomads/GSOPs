import hou
import inspect
import json
from pathlib import Path

from gsops.settings import apply_settings

GSOPS_PATH = hou.text.expandString("$GSOPS") or str(Path(inspect.getfile(inspect.currentframe())).parent.parent)
GSOPS_LICENSE_FILE_PATH = f"{GSOPS_PATH}/.gsops/license"
GSOPS_CONFIG_FILE_PATH = f"{GSOPS_PATH}/.gsops/config.json"


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
    
    geo_node = None
    try:
        geo_node = hou.node("/obj").createNode("geo", "__gsops_auth_tmp__")
        dummy_node = geo_node.createNode("sphere")
        auth_node = geo_node.createNode("GSplatAuth")
        auth_node.setInput(0, dummy_node)
        try:
            auth_node.cook(force=True)
        except Exception:
            # No need to print anything since there is already an error message on terminal
            pass
    finally:
        if geo_node and geo_node.parent():
            try:
                geo_node.destroy()
            except Exception:
                print("GSOPs: Authentication cleanup failed.")
                pass

    if not hasattr(hou.session, "gsops"):
        return 0
    return hou.session.gsops["auth_level"]


def setup_for_authentication_level(level=0):
    # 1) Apply main plugin settings
    apply_settings()

    # 2) Setup node visibility
    # Unhide all otls...
    all_node_type_categories = hou.nodeTypeCategories().keys()
    for node_type_category in all_node_type_categories:
        node_category = hou.nodeTypeCategories().get(node_type_category) 
        for node_type_name, node_type in node_category.nodeTypes().items():
            if not node_type_name.startswith("gsop::"):
                continue
            node_type.setHidden(False)
    # Retrieve config to determine visibility of nodes...
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


