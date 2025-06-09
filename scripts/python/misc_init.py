import hou


def add_gsops_shelf():
    if not hou.isUIAvailable():
        return
    gsops_shelf = hou.shelves.shelves()['gsops_shelf']
    shelf_set_1 = hou.shelves.shelfSets()['shelf_set_1']
    shelves_in_set_1 = list(shelf_set_1.shelves())
    if gsops_shelf not in shelves_in_set_1:
        shelves_in_set_1 += [gsops_shelf] 
        shelf_set_1.setShelves(shelves_in_set_1)
