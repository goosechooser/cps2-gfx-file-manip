from abc import ABCMeta, abstractmethod

class FileFormat(object):
    __metaclass__ = ABCMeta

    def __init__(self, verbose):
        self._verbose = verbose
        self.verboseprint = print if self._verbose else lambda *a, **k: None

    @abstractmethod
    def interleave_files(self):
        pass

    @abstractmethod
    def deinterleave_file(self):
        pass
