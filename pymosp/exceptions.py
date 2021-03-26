# -*- coding: utf-8 -*-


class PyMOSPError(Exception):
    def __init__(self, message):
        super(PyMOSPError, self).__init__(message)
        self.message = message


class NoURL(PyMOSPError):
    pass
