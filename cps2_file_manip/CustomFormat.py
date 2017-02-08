import os
import sys
import os.path
from cps2_file_manip.file_manip import interleave, deinterleave
from cps2_file_manip.FileFormat import FileFormat

#Saving file(s) notes:
#deinter -> FILENAME.even / FILENAME.odd
#inter -> concat 2 file names and add 'combined' to end
#both will save to cwd, unless specified
#use these options if user doesnt give input


#Other possible names, GenericFormat / NoFormat ?
class CustomFormat(FileFormat):
    def open_file(self, filepath):
        """Error handling. Returns bytearray of data in file"""
        try:
            with open(filepath, 'rb') as f:
                return bytearray(f.read())
        except FileNotFoundError as error:
            print(error, file=sys.stderr)
            sys.exit(1)

    #prime candidate for some R E F A C T O R I N G
    def save_file(self, data, operation):
        if operation == 'interleave':
            #if no custom output, save to cwd with default name
            if not self._savepaths:
                fnames = [os.path.split(fname)[1] for fname in self._filepaths]
                spath = '.'.join([*fnames, 'combined', 'bin'])

            #if custom output is a folder, save default file name to that location
            elif os.path.isdir(self._savepaths[0]):
                head = self._savepaths[0]
                fnames = [os.path.split(fname)[1] for fname in self._filepaths]
                tail = '.'.join([*fnames, 'combined', 'bin'])
                spath = os.path.join(head, tail)

            #else use given output
            else:
                spath = self._savepaths[0]

            with open(spath, 'wb') as f:
                self.verboseprint('Saving', spath)
                f.write(data)

        elif operation == 'deinterleave':
            #if no custom output, save to cwd with default name
            if not self._savepaths:
                fname = [os.path.split(fname)[1] for fname in self._filepaths]
                spaths = ['.'.join([fname[0], str(i), 'bin']) for i in range(self._nsplit)]

            #if custom output is a folder, save default file name to that location
            elif os.path.isdir(self._savepaths[0]):
                head = self._savepaths[0]
                fname = os.path.split(self._filepaths[0])[1]
                tails = ['.'.join([fname, str(i), 'bin']) for i in range(self._nsplit)]
                spaths = [os.path.join(head, tail) for tail in tails]

            #if custom output is a file, append number to the end of it
            else:
                spaths = ['.'.join([self._savepaths[0], str(i), 'bin']) for i in range(self._nsplit)]

                #investigate whether multiple custom output names is necessary
                # else:
                #     spaths = ['.'.join([self._savepaths[i], str(i)]) for i in range(self._nsplit)]

            for i, savepath in enumerate(spaths):
                with open(savepath, 'wb') as f:
                    self.verboseprint('Saving', savepath)
                    f.write(data[i])
        else:
            print('probably an error here')

    def interleave_files(self):
        self.verboseprint('Opening files')
        data = [self.open_file(fp) for fp in self._filepaths]

        self.verboseprint('Interleaving files every', self._numbytes, 'bytes')
        interleave_data = interleave(data, self._numbytes)

        self.save_file(interleave_data, 'interleave')

    def deinterleave_file(self):
        self.verboseprint('Opening file')
        fdata = self.open_file(self._filepaths[0])

        self.verboseprint('Deinterleaving files every', self._numbytes, 'bytes')
        deinterleave_data = deinterleave(fdata, self._numbytes, self._nsplit)

        self.save_file(deinterleave_data, 'deinterleave')
