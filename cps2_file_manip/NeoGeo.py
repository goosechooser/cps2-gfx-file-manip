import os
import sys
from cps2_file_manip.file_manip import interleave, deinterleave
from cps2_file_manip.FileFormat import FileFormat

#file name scheme like
#"002-c1.c1" "002-c2.c2" "002-c3.c3" "002-c4.c4"
#always in pairs
class NeoGeo(FileFormat):
    def _format_fname(self, name, i):
        try:
            tailsplit = name.split('-')
        except IndexError:
            error = 'is an invalid file name. Files should be formatted like \'BASE-c1.c1\''
            print(name, error, file=sys.stderr)
            sys.exit(1)

        basename = tailsplit[0]
        fnum = int(tailsplit[1].split('.')[-1][-1]) + i

        fname = '.'.join(['c' + str(fnum)] * 2)
        return '-'.join([basename, fname])

    def _get_file_data(self, filepath):
        #check how many files were specified
        #for now just testing case of 1 file
        head, tail = os.path.split(filepath)

        to_split = []
        fnames = []

        for i in range(2):
            fname = self._format_fname(tail, i)
            try:
                with open(os.path.join(head, fname), 'rb') as f:
                    to_split.append(bytearray(f.read()))
            except FileNotFoundError as error:
                print(error, file=sys.stderr)
                sys.exit(1)

            fnames.append(fname)

        return fnames, to_split

    def _combine_file_names(self, fnames):
        fsplit = [os.path.split(name)[1] for name in fnames]
        base = fsplit[0].split('-')[0]
        fnums = [name.split(".")[-1] for name in fsplit]
        comb_fnums = '.'.join([*fnums, 'combined'])

        return '-'.join([base, comb_fnums])

    def interleave_files(self, fnames, verbose=False):
        verboseprint = print if verbose else lambda *a, **k: None
        # for fname in fnames:
        #     print('neogeo ', fname)
        names, to_interleave = self._get_file_data(fnames)
        verboseprint('interleaving', *[n for n in names])

        interleaved = interleave(to_interleave[0], to_interleave[1], 1)

        head = os.path.split(fnames)[0]
        comb_fname = self._combine_file_names(names)

        print("interleaved file", os.path.join(head, comb_fname), "created")

        with open(os.path.join(head, comb_fname), 'wb') as f:
            f.write(interleaved)

    def deinterleave_file(self, fname, verbose=False):
        head, tail = os.path.split(fname)
        split_tail = tail.split('-')
        base = split_tail[0]
        fnames = ['-'.join([base, '.'.join([name] * 2)]) for name in split_tail[1].split('.')[:-1]]
        print(fnames)

        try:
            with open(fname, 'rb') as f:
                data = bytearray(f.read())
        except FileNotFoundError as error:
            print(error, file=sys.stderr)
            sys.exit(1)

        print("deinterleaving", tail)

        deinterleaved = deinterleave(data, 1)

        for i, fname in enumerate(fnames):
            print("deinterleaved file", fname, "created")

            with open(os.path.join(head, fname), 'wb') as f:
                f.write(deinterleaved[i])

if __name__ == '__main__':
    inputf = 'breakrevgfx/245-c1.c1'
    inputd = 'breakrevgfx/245-c1.c2.combined'
    temp = NeoGeo()
    temp.interleave_files(inputf, verbose=True)
    #temp.deinterleave_file(inputd)
