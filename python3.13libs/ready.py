import os
import hou
import importlib.util
from pathlib import Path
import inspect

GSOPS_BASE_PATH = Path(hou.getenv("GSOPS") or str(Path(inspect.getfile(inspect.currentframe())).parent.parent))

misc_init_module_path = GSOPS_BASE_PATH / "scripts/python/misc_init.py"
misc_init_module_spec = importlib.util.spec_from_file_location("misc_init", misc_init_module_path)
misc_init = importlib.util.module_from_spec(misc_init_module_spec)
misc_init_module_spec.loader.exec_module(misc_init)
misc_init.init()

should_disable_popup = os.environ.get("GSOPS_DISABLE_POPUP", False).lower() in ('true', '1')
if not should_disable_popup:
    popup_init_module_path = GSOPS_BASE_PATH / "scripts/python/popup_init.py"
    popup_init_module_spec = importlib.util.spec_from_file_location("popup_init", popup_init_module_path)
    popup_init = importlib.util.module_from_spec(popup_init_module_spec)
    popup_init_module_spec.loader.exec_module(popup_init)
    popup_init.show()

print("GSOPs has been initialized.")