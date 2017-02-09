import sys
from abc import ABCMeta, abstractmethod

class FileFormat(object):
    __metaclass__ = ABCMeta

    def __init__(self, filepaths, numbytes, savepaths, verbose=False):
        self._verbose = verbose
        self.verboseprint = print if self._verbose else lambda *a, **k: None
        self._filepaths = filepaths
        self._numbytes = numbytes
        self._savepaths = savepaths
        self._nsplit = 1

    @abstractmethod
    def interleave_files(self):
        pass

    @abstractmethod
    def deinterleave_file(self):
        pass

    @property
    def nsplit(self):
        return self._nsplit

    @nsplit.setter
    def nsplit(self, value):
        self._nsplit = value

    @staticmethod
    def open_file(filepath):
        """Error handling. Returns bytearray of data in file"""
        try:
            with open(filepath, 'rb') as f:
                return bytearray(f.read())
        except FileNotFoundError as error:
            print(error, file=sys.stderr)
            sys.exit(1)
