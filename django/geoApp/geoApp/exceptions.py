from requests.exceptions import RequestException

class NotAZipFileError(Exception):
    pass

class NotAShapefileError(Exception):
    pass

class NoShapeFileFoundError(Exception):
    pass

class TooManyShapeFileFoundError(Exception):
    pass

class UncoherentConfigurationsError(Exception):
    pass

class GeoserverNotRespondingError(RequestException):
    # cannot get any response
    pass

class GeoserverNotAvailableError(RequestException):
    # generic
    pass