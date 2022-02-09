class PAKFileFormatError(Exception):
    pass


class PAKFileZippingError(Exception):
    pass


class PAKFileUnzippingError(Exception):
    pass


class PAKMismatchedCRC(Exception):
    pass


class UtilPermissionError(Exception):
    pass


class DirectoryError(Exception):
    pass


class MenuSelectionError(Exception):
    pass


class ApplicationError(Exception):
    pass
