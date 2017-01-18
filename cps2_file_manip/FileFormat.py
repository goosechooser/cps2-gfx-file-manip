from abc import ABCMeta, abstractmethod

class FileFormat(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def interleave_files(self):
        pass

    @abstractmethod
    def deinterleave_file(self):
        pass
