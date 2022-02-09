## Imports
from os import system, path, scandir, makedirs
from ctypes import windll
from datetime import datetime
from errno import EEXIST
from src.colors import colors as c
import sys


## Pre-Main
def cls():
    system("cls")


def get_input(prompt: str = "Example Prompt: "):
    return str(input(prompt))


def pause(mode=0):
    if mode == 0:
        system("pause")
    elif mode == 1:
        system("pause>nul")
    else:
        print("Nope.")


def adminCheck():
    try:
        from os import getuid
        is_admin = getuid() == 0
        return is_admin
    except (AttributeError, NameError, ImportError):
        is_admin = windll.shell32.IsUserAnAdmin() != 0
        return is_admin


def dataToBytes(data):
    if isinstance(data, bytes):
        return data
    else:
        return data.encode('utf-8')


def bytesToData(data):
    if isinstance(data, bytes):
        return data.decode('utf-8')
    else:
        return data


def getFmtTime(mode=0):
    if mode == 0:
        now = datetime.now()
        timeStamp = now.strftime("%H:%M:%S")
        fullTimeStamp = "[" + timeStamp + "]"
        return fullTimeStamp
    else:
        print("Not supported at this time.")
        return "Nope."


def getFmtDate(mode=0):
    if mode == 0:
        now = datetime.now()
        dateStamp = now.strftime("%Y/%m/%d")
        fullDateStamp = "[" + dateStamp + "]"
        return fullDateStamp
    else:
        print("Not supported at this time.")
        return "Nope."


def get_file_size(pathLink: str = "C:\Windows\system32\cmd.exe"):
    try:
        return path.getsize(pathLink)
    except:
        return 0


def get_directory_size(pathLink: str = "C:\Windows\system32"):
    try:
        total = 0
        try:
            for entry in scandir(pathLink):
                if entry.is_file():
                    total += entry.stat().st_size
                elif entry.is_dir():
                    total += get_directory_size(entry.path)
        except NotADirectoryError:
            return path.getsize(pathLink)
        except PermissionError:
            return 0
        return total
    except:
        return 0


def human_format(num):
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '%.2f %s' % (num, ['', 'Thousand', 'Million', 'Billion', 'Trillion', 'Pentillion'][magnitude])


def human_size(bytes, units=(' bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB')):
    """ Returns a human readable string reprentation of bytes"""
    return str(bytes) + ' ' + units[0] if bytes < 1024 else human_size(bytes >> 10, units[1:])


def human_sizeC(num):
    magnitude = 0
    while abs(num) >= 1024:
        magnitude += 1
        num /= 1024.0
    return "%.2f %s" % (num, ['bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB'][magnitude])


def dynamic_resize(toSize: str = "Testing String", splitSize: int = 4):
    currentLength = len(toSize)
    fq = int(currentLength) / splitSize
    lq = int(currentLength) - fq
    return f"{toSize[0:int(fq)]}...{toSize[int(lq):]}"


def mkdirp(path_to_mk):
    try:
        makedirs(path_to_mk, exist_ok=True)
    except OSError as exc:
        if exc.errno == EEXIST and path.isdir(path_to_mk):
            pass
        else:
            raise


def clearColor():
    print(c.END)


def setTitle(title):
    system(f"title {title}")


def qExit():
    cls()
    sys.exit()