import os
import sys
from cps2_file_manip.file_manip import interleave, deinterleave
from cps2_file_manip.FileFormat import FileFormat

#Saving file(s) notes:
#deinter -> FILENAME.even / FILENAME.odd
#inter -> concat 2 file names and add 'combined' to end
#both will save to cwd, unless specified
#use these options if user doesnt give input


#Other possible names, GenericFormat / NoFormat ?
class CustomFormat(FileFormat):
    #things to track:
    #filepaths(1-2?), num of bytes to interleave by, where to save file(s)
    def __init__(self, filepaths, numbytes, savepaths, verbose=False):
        self._filepaths = filepaths
        self._numbytes = numbytes
        #Place holder until I figure out a better way to determine whats being done
        self._savepaths = savepaths
        super(CustomFormat, self).__init__(verbose)

    def open_file(self, filepath):
        """Error handling. Returns bytearray of data in file"""
        try:
            with open(filepath, 'rb') as f:
                return bytearray(f.read())
        except FileNotFoundError as error:
            print(error, file=sys.stderr)
            sys.exit(1)

    def save_file(self, data, operation):
        #unsure what exceptions may arise during writing to a file
        if operation == 'interleave':
            #should probably check if its a folder or file
            #if folder construct default name
            if not self._savepaths:
                fnames = [os.path.split(fname)[1] for fname in self._filepaths]
                self._savepaths = ['.'.join([*fnames, 'combined'])]

            with open(*self._savepaths, 'wb') as f:
                self.verboseprint('Saving', *self._savepaths)
                f.write(data)

        elif operation == 'deinterleave':
            if not self._savepaths:
                fname = [os.path.split(fname)[1] for fname in self._filepaths]
                self._savepaths = ['.'.join([fname[0], 'even']), '.'.join([fname[0], 'odd'])]

            with open(self._savepaths[0], 'wb') as f:
                self.verboseprint('Saving', self._savepaths[0])
                f.write(data[0])

            with open(self._savepaths[1], 'wb') as f:
                self.verboseprint('Saving', self._savepaths[1])
                f.write(data[1])

        else:
            print('probably an error here')

    #Currently only interleaves 2 files together
    #How many interleaving more than 2 files be handled / should it be handled?
    def interleave_files(self):
        self.verboseprint('Opening files')
        fdata1 = self.open_file(self._filepaths[0])
        fdata2 = self.open_file(self._filepaths[1])

        self.verboseprint('Interleaving files every', self._numbytes, 'bytes')
        interleave_data = interleave(fdata1, fdata2, self._numbytes)

        self.save_file(interleave_data, 'interleave')

    def deinterleave_file(self):
        self.verboseprint('Opening file')
        fdata = self.open_file(self._filepaths[0])

        self.verboseprint('Deinterleaving files every', self._numbytes, 'bytes')
        deinterleave_data = deinterleave(fdata, self._numbytes)

        self.save_file(deinterleave_data, 'deinterleave')

def cli_interleave(file1, file2, numbytes, savepath=None):
    formatter = CustomFormat([file1, file2], numbytes, savepath)
    # fdata1 = formatter.open_file(file1)
    # fdata2 = formatter.open_file(file2)

    # #data = formatter.interleave_files(file1, file2, 1)
    # data = interleave(fdata1, fdata2, 1)
    # formatter.save_file(data, 'interleave')

def cli_deinterleave(file_, numbytes, savepath=None):
    formatter = CustomFormat([file_], numbytes, savepath, True)
    # fdata = formatter.open_file(self.filepath[0])

    # data = deinterleave(fdata, self._num_bytes)
    # formatter.save_file(data, 'deinterleave')

if __name__ == '__main__':
    filea = 'breakrevgfx/245-c1.c1'
    fileb = 'breakrevgfx/245-c2.c2'
    saveas = 'breakrevgfx/test.hello'

    #cli_interleave(filea, fileb, 1, savepath=saveas)
    # cli_deinterleave(saveas, 1)
