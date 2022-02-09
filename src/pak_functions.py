import zipfile
from zipfile import ZipFile, is_zipfile
from os import walk, path
from src.util_functions import mkdirp, get_file_size, get_directory_size, human_sizeC, clearColor
from src.exceptions import PAKFileFormatError, PAKMismatchedCRC, PAKFileZippingError, PAKFileUnzippingError
from src.colors import colors as c


def get_folder_size(folder_path: str):
    return str(human_sizeC(get_directory_size(folder_path)))


def get_size_of_file(file_path: str):
    return str(human_sizeC(get_file_size(file_path)))


def check_pak_validity(input_pakfile: str):
    is_zip = is_zipfile(input_pakfile)
    if not is_zip:
        raise PAKFileFormatError(f"Invalid Format - This File is NOT a PAKFile! ({input_pakfile})")
    try:
        with ZipFile(input_pakfile, 'r') as zip:
            results_of_test = zip.testzip()
    except zipfile.BadZipfile as e:
        raise PAKFileFormatError(f"Invalid Format - This File is NOT a PAKFile! ({input_pakfile + ' - ' + e})")
    if results_of_test is not None:
        raise PAKMismatchedCRC("Corruption - There is a CRC or File Header Mismatch in the PAKFile!")
    return is_zip, results_of_test


def find_all_files_recursive(directory: str):
    file_paths = []
    for root, directories, files in walk(directory):
        for filename in files:
            filepath = path.join(root, filename)
            file_paths.append(filepath)
    return file_paths


def write_to_pakfile(input_directory: str = "./", output_name: str = "data2.pak"):
    try:
        file_paths = []
        for root, directories, files in walk(input_directory):
            for filename in files:
                filepath = path.join(root, filename)
                file_paths.append(filepath)

        print("\nThe Following Files will be PAK'ed:")
        for file_name in file_paths:
            print(c.PURPLE + file_name)
        clearColor()

        with ZipFile(output_name, 'w', zipfile.ZIP_DEFLATED) as zipobj:
            length = len(input_directory)
            for root, directories, files in walk(input_directory):
                folder = root[length:]
                for filename in files:
                    zipobj.write(path.join(root, filename), path.join(folder, filename))
    except:
        raise PAKFileZippingError("An error occurred whilst generating the PAK File!")


def read_from_zipfile(input_pakfile: str):
    with ZipFile(input_pakfile, 'r') as zipobj:
        zipobj.printdir()


def extract_zipfile(input_pakfile: str, output_path: str):
    try:
        mkdirp(output_path)
        with ZipFile(input_pakfile, 'r') as zipobj:
            zipobj.extractall(path=output_path)
    except:
        raise PAKFileUnzippingError("An error occurred whilst extracting the PAK File!")
