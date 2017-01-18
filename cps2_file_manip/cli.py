import os
import argparse
from struct import Struct
from . import file_manip

#GFX files (for cps2) seem to always be in batches of 4
#workflow along the lines of 
#point at first file (in batch of 4)
#grap the four files
#interleave the 4 in one go
def main():
    parser = argparse.ArgumentParser(description='(de)interleave cps2 graphics files.')
    operations = parser.add_mutually_exclusive_group()
    operations.add_argument('-i', '--interleave', action='store_true',
                            help='interleave the files together')
    operations.add_argument('-d', '--deinterleave', action='store_true',
                            help='deinterleave the combined file')
    parser.add_argument('file', type=str,
                        help='first file to interleave or combined file to deinterleave')

    parser.add_argument('-v', '--verbose', action='store_true',
                        help='make it wordy')
    args = parser.parse_args()

    if args.interleave:
        file_manip.interleave_cps2(args.file, verbose=args.verbose)
    elif args.deinterleave:
        file_manip.deinterleave_cps2(args.file, verbose=args.verbose)
    else:
        print('no operation selected')