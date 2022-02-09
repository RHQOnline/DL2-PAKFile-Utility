from src.pak_functions import write_to_pakfile, read_from_zipfile, extract_zipfile, check_pak_validity, \
    get_folder_size, get_size_of_file
from src.util_functions import cls, setTitle, qExit, pause, adminCheck, get_input, clearColor
from src.exceptions import UtilPermissionError, MenuSelectionError
from src.colors import colors as c
from src.app_config import _version, _developer, _github_url, _app_name


def do_check_for_admin():
    if adminCheck():
        main_menu()
    else:
        raise UtilPermissionError("The PAKFile Utility isn't being ran as an Administrator!")


def main_menu():
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
        selection = get_input("\nChoice: " + c.LIGHT_PURPLE)
        clearColor()
        if selection.isdigit():
            selection = int(selection)
            if 0 < selection <= 4:
                if selection == 1:
                    examine_pakfile()
                elif selection == 2:
                    extract_pakfile()
                elif selection == 3:
                    create_pakfile()
                elif selection == 4:
                    qExit()
            else:
                raise MenuSelectionError(f"Invalid Menu Selection: Out of Bounds [1-4] ({selection})")
        else:
            raise MenuSelectionError(f"Invalid Menu Selection: Integer Not Supplied ({selection})")


def validity_check(file):
    validity, errors = check_pak_validity(file)
    print(f"PAKFile Validity: {(c.GREEN + str(validity) + c.END) if validity else (c.RED + str(validity) + c.END)}\nPAKFile Content Errors: {(c.GREEN + str(errors) + c.END) if errors is None else (c.RED + str(errors) + c.END)}\n")


def examine_pakfile():
    fname = get_input("Enter File Name: " + c.LIGHT_RED)
    clearColor()
    print(f"Size of '{fname}': {c.BOLD + c.CYAN + get_size_of_file(fname) + c.END}\n")
    validity_check(fname)
    pause()
    print("")
    read_from_zipfile(fname)
    print("")
    pause()


def create_pakfile():
    folder = get_input("Enter Folder Path: " + c.LIGHT_RED)
    pakname = get_input(c.END + "Enter PAKFile Path and Name: " + c.LIGHT_RED)
    clearColor()
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
    read_from_zipfile(fname)
    extract_zipfile(fname, opath)
    print(f"\nSize of '{opath}': {c.BOLD + c.CYAN + get_folder_size(opath) + c.END}\n")
    pause()


if __name__ == "__main__":
    setTitle("Dying Light 2 PAKFile Utility")
    do_check_for_admin()
