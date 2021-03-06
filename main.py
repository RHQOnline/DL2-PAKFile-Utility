from src.pak_functions import write_to_pakfile, read_from_zipfile, extract_zipfile, check_pak_validity, \
    get_folder_size, get_size_of_file
from src.util_functions import cls, setTitle, qExit, pause, adminCheck, get_input, clearColor
from src.exceptions import UtilPermissionError, MenuSelectionError
from src.colors import colors as c
from src.app_config import _version, _developer, _github_url, _app_name


_last_pak_name = None
_last_pak_folder_path = None
_max_selection_int = 4


def do_check_for_admin():
    if adminCheck():
        main_menu()
    else:
        print(f"Please run the {c.FAIL + _app_name + c.END} as an {c.LIGHT_CYAN + 'Administrator' + c.END}!")
        pause()
        qExit()
        # raise UtilPermissionError("The PAKFile Utility isn't being ran as an Administrator!")


def main_menu():
    global _last_pak_name, _last_pak_folder_path, _max_selection_int
    x = True
    while x:
        cls()
        print(f"Welcome to the {c.FAIL + _app_name + ' ' + c.OKGREEN + _version + c.END}!")
        print(f"This tool was made by {c.ORANGE + _developer + c.END} and is proudly {c.LIGHT_WHITE}open-source{c.END}!")
        print(f"View and contribute to it's source-code at {c.OKBLUE + _github_url + c.END}.\n")
        print(f"[{c.GREEN}1{c.END}] {c.LIGHT_GREEN}Examine PAKFile{c.END}")
        print(f"[{c.GREEN}2{c.END}] {c.LIGHT_GREEN}Extract PAKFile{c.END}")
        print(f"[{c.GREEN}3{c.END}] {c.LIGHT_GREEN}Build PAKFile{c.END}")
        print(f"[{c.GREEN}4{c.END}] {c.LIGHT_GREEN}Exit Application{c.END}")
        if _last_pak_name is not None:
            print(f"[{c.BLUE}5{c.END}] {c.LIGHT_BLUE}Rebuild Last PAKFile{c.END}")
            print(f"[{c.RED}6{c.END}] {c.LIGHT_RED}Clear Rebuild Cache{c.END}")
        selection = get_input("\nChoice: " + c.LIGHT_PURPLE)
        clearColor()
        if selection.isdigit():
            selection = int(selection)
            if 0 < selection <= 6:
                if selection == 1:
                    examine_pakfile()
                elif selection == 2:
                    extract_pakfile()
                elif selection == 3:
                    create_pakfile()
                elif selection == 4:
                    qExit()
                elif _last_pak_name is not None and selection == 5:
                    quick_create_pakfile(_last_pak_name, _last_pak_folder_path)
                elif _last_pak_name is not None and selection == 6:
                    _last_pak_name = None
                    _last_pak_folder_path = None
                    _max_selection_int = 4
                else:
                    print(f"Invalid Menu Selection: Out of Bounds [1-{_max_selection_int}] ({c.FAIL + str(selection) + c.END})!")
                    pause()
                    # raise MenuSelectionError(f"Invalid Menu Selection: Out of Bounds [1-4] ({selection})")
            else:
                print(f"Invalid Menu Selection: Out of Bounds [1-{_max_selection_int}] ({c.FAIL + str(selection) + c.END})!")
                pause()
                # raise MenuSelectionError(f"Invalid Menu Selection: Out of Bounds [1-4] ({selection})")
        else:
            print(f"Invalid Menu Selection: Integer Not Supplied ({c.RED + selection + c.END})")
            pause()
            # raise MenuSelectionError(f"Invalid Menu Selection: Integer Not Supplied ({selection})")


def validity_check(file):
    validity, errors = check_pak_validity(file)
    print(f"PAKFile Validity: {(c.GREEN + 'Valid' + c.END) if validity else (c.RED + 'Invalid' + c.END)}\nPAKFile Content Errors: {(c.GREEN + str(errors) + c.END) if errors is None else (c.RED + str(errors) + c.END)}\n")


def examine_pakfile():
    fname = get_input("Enter File Name: " + c.LIGHT_RED)
    clearColor()
    print(f"Size of '{fname}': {c.BOLD + c.CYAN + get_size_of_file(fname) + c.END}\n")
    validity_check(fname)
    pause()
    print("")
    try:
        read_from_zipfile(fname)
        print("")
        pause()
    except:
        ...


def create_pakfile():
    global _last_pak_name, _last_pak_folder_path, _max_selection_int
    folder = get_input("Enter Folder Path: " + c.LIGHT_RED)
    pakname = get_input(c.END + "Enter PAKFile Path and Name: " + c.LIGHT_RED)
    clearColor()
    print(f"Size of '{folder}': {c.BOLD + c.CYAN + get_folder_size(folder) + c.END}\n")
    pause()
    write_to_pakfile(folder, pakname)
    print(f"Size of '{pakname}': {c.BOLD + c.CYAN + get_size_of_file(pakname) + c.END}\n")
    validity_check(pakname)
    print("All Files PAK'ed Successfully!\n")
    _last_pak_name = pakname
    _last_pak_folder_path = folder
    _max_selection_int = 6
    pause()


def quick_create_pakfile(pakname, folder):
    print(f"Size of '{folder}': {c.BOLD + c.CYAN + get_folder_size(folder) + c.END}\n")
    pause()
    write_to_pakfile(folder, pakname)
    print(f"Size of '{pakname}': {c.BOLD + c.CYAN + get_size_of_file(pakname) + c.END}\n")
    validity_check(pakname)
    print("All Files PAK'ed Successfully!\n")
    pause()


def extract_pakfile():
    fname = get_input("Enter File Name: " + c.LIGHT_RED)
    opath = get_input(c.END + "Enter Output Path: " + c.LIGHT_RED)
    clearColor()
    print(f"Size of '{fname}': {c.BOLD + c.CYAN + get_size_of_file(fname) + c.END}\n")
    validity_check(fname)
    try:
        read_from_zipfile(fname)
        extract_zipfile(fname, opath)
        print(f"\nSize of '{opath}': {c.BOLD + c.CYAN + get_folder_size(opath) + c.END}\n")
        pause()
    except:
        pause()


if __name__ == "__main__":
    setTitle("Dying Light 2 PAKFile Utility")
    do_check_for_admin()
