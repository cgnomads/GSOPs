import hou
import gsops.authentication as auth


def _add_gsops_shelf():
    if not hou.isUIAvailable():
        return

    try:
        gsops_shelf = hou.shelves.shelves()['gsops_shelf']
    except KeyError:
        print("Could not find 'gsops_shelf'.")
        return

    try:
        shelf_set_1 = hou.shelves.shelfSets()['shelf_set_1']
    except KeyError:
        print("Could not find 'shelf_set_1'.")
        return

    # Filter out any deleted shelves safely
    valid_shelves = []
    shelf_names = []
    for shelf in shelf_set_1.shelves():
        try:
            name = shelf.name()
            valid_shelves.append(shelf)
            shelf_names.append(name)
        except hou.ObjectWasDeleted:
            continue

    if gsops_shelf.name() not in shelf_names:
        valid_shelves.append(gsops_shelf)
        shelf_set_1.setShelves(valid_shelves)


def _attempt_authentication_and_setup():
    auth.setup_for_authentication_level(auth.authenticate())


def init():
    if hou.isUIAvailable():
        _add_gsops_shelf()
        _attempt_authentication_and_setup()
