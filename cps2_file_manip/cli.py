import argparse
#from . import cps2
from cps2_file_manip.NeoGeo import NeoGeo
from cps2_file_manip.CustomFormat import CustomFormat

def test_main():
    parser = argparse.ArgumentParser(description='(de)interleave binary files.')
    parser.add_argument('files', type=str, nargs='*',
                        help='1 file to deinterleave, 2 files to interleave')
    parser.add_argument('numbytes', type=int,
                        help='number of bytes to (de)interleave by')
    parser.add_argument('-s', '--saveas', type=str, nargs='*',
                        help='specify where to save output, default is current working directory')
    parser.add_argument('-f', '--format', type=str,
                        help='specify a file format, options are: \'cps2\' or \'neogeo\'')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='make it wordy')

    args = parser.parse_args()
    print(args)

    #Do special things wrt how saved files are named for neogeo and cps2
    if args.format == 'neogeo':
        formatter = NeoGeo(args.verbose)
    else:
        formatter = CustomFormat(args.files, args.numbytes, args.saveas, verbose=args.verbose)

    #Right now only handles 1 or 2 files
    #Eventually ... more?
    if len(args.files) == 1:
        formatter.deinterleave_file()
    elif len(args.files) == 2:
        formatter.interleave_files()
    else:
        print('ruh o')
