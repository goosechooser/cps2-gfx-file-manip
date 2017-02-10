import argparse
#from . import cps2
#from cps2_file_manip.NeoGeo import NeoGeo
from cps2_file_manip.CustomFormat import CustomFormat

#works great except cps2-manip is now asking for byte size
#FIX IT ^^^^

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def bswap_main():
    parser = argparse.ArgumentParser(description='swaps bytes on a given basis')
    parser.add_argument('file', type=str,
                        help='input file')
    parser.add_argument('format', type=str,
                        help="""format to use when byte swapping.
                        possible formats are: 16 bits - h, H;
                        32 bits - l, L, i, I; 64 bits - q, Q
                        more information can be found at: 
                        https://docs.python.org/3/library/struct.html#format-characters""")
    parser.add_argument('-o', '--output', type=str,
                        help='specify where to save output, default is current working directory')
    args = parser.parse_args()
    #fill in the rest

def unfman_main():
    parser = argparse.ArgumentParser(description='(de)interleave binary files.')
    parser.add_argument('files', type=str, nargs='*',
                        help="""1 file and a number (how many files to output) to deinterleave,
                        more than 1 file to interleave
                        ex: FILE 2 will deinterleave FILE every 2 bytes into 2 files
                        ex: FILE1 FILE2 FILE3 4 will interleave the files every 4 bytes""")
    parser.add_argument('numbytes', type=int,
                        help='number of bytes to (de)interleave by')
    parser.add_argument('-o', '--output', type=str,
                        help='specify where to save output, default is current working directory')
    # parser.add_argument('-f', '--format', type=str,
    #                     help='specify a file format, options are: \'cps2\' or \'neogeo\'')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='make it wordy')

    args = parser.parse_args()
    #print(args)
    #print(len(args.files))

    #Do special things wrt how saved files are named for neogeo and cps2
    # if args.format == 'neogeo':
    #     # formatter = NeoGeo(args.verbose)
    #     print('ok')
    # else:
    formatter = CustomFormat(args.files, args.numbytes, args.output, verbose=args.verbose)

    #Will probably want to move this logic to the __init__ of the formatter
    if len(args.files) == 2:
        #this will probably run into an issue if someone has a file that is just a single number
        if is_number(args.files[1]):
            formatter.nsplit = int(args.files[1])
            formatter.deinterleave_file()
        else:
            formatter.interleave_files()
    elif len(args.files) > 2:
        formatter.interleave_files()
    else:
        print('ruh o')
