import argparse
#from . import cps2
#from cps2_file_manip.NeoGeo import NeoGeo
from cps2_file_manip.CustomFormat import CustomFormat

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def main():
    parser = argparse.ArgumentParser(description='(de)interleave binary files.')
    parser.add_argument('files', type=str, nargs='*',
                        help="""1 file and a number (how many files to output) to deinterleave,
                        more than 1 file to interleave""")
    parser.add_argument('numbytes', type=int,
                        help='number of bytes to (de)interleave by')
    parser.add_argument('-o', '--output', type=str, nargs='*',
                        help='specify where to save output, default is current working directory')
    parser.add_argument('-f', '--format', type=str,
                        help='specify a file format, options are: \'cps2\' or \'neogeo\'')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='make it wordy')

    args = parser.parse_args()
    #print(args)
    #print(len(args.files))

    #Do special things wrt how saved files are named for neogeo and cps2
    if args.format == 'neogeo':
        # formatter = NeoGeo(args.verbose)
        print('ok')
    else:
        formatter = CustomFormat(args.files, args.numbytes, args.output, verbose=args.verbose)

    #check if custom save place is a folder!!!
    if len(args.files) == 2:
        print(args.files[0])
        if is_number(args.files[1]):
            formatter.nsplit = int(args.files[1])
            formatter.deinterleave_file()
        else:
            formatter.interleave_files()
    elif len(args.files) > 2:
        formatter.interleave_files()
    else:
        print('ruh o')
