import argparse
from . import cps2
from cps2_file_manip.NeoGeo import NeoGeo

# def cps2_main():
#     parser = argparse.ArgumentParser(description='(de)interleave cps2 graphics files.')
#     operations = parser.add_mutually_exclusive_group()
#     operations.add_argument('-i', '--interleave', action='store_true',
#                             help='interleave the files together')
#     operations.add_argument('-d', '--deinterleave', action='store_true',
#                             help='deinterleave the combined file')
#     parser.add_argument('file', type=str,
#                         help='first file to interleave or combined file to deinterleave')

#     parser.add_argument('-v', '--verbose', action='store_true',
#                         help='make it wordy')
#     args = parser.parse_args()

#     if args.interleave:
#         cps2.interleave_files(args.file, verbose=args.verbose)
#     elif args.deinterleave:
#         cps2.deinterleave_file(args.file, verbose=args.verbose)
#     else:
#         print('no operation selected')

# def neogeo_main():
#     parser = argparse.ArgumentParser(description='(de)interleave neo geo graphics files.')
#     operations = parser.add_mutually_exclusive_group()
#     operations.add_argument('-i', '--interleave', action='store_true',
#                             help='interleave the files together')
#     operations.add_argument('-d', '--deinterleave', action='store_true',
#                             help='deinterleave the combined file')
#     parser.add_argument('file', type=str,
#                         help='first file to interleave or combined file to deinterleave')

#     parser.add_argument('-v', '--verbose', action='store_true',
#                         help='make it wordy')
#     args = parser.parse_args()

#     if args.interleave:
#         neogeo.interleave_files(args.file, verbose=args.verbose)
#     elif args.deinterleave:
#         neogeo.deinterleave_file(args.file, verbose=args.verbose)
#     else:
#         print('no operation selected')

def test_main():
    parser = argparse.ArgumentParser(description='(de)interleave neo geo graphics files.')
    operations = parser.add_mutually_exclusive_group()
    operations.add_argument('-i', '--interleave', action='store_true',
                            help='interleave the files together')
    operations.add_argument('-d', '--deinterleave', action='store_true',
                            help='deinterleave the combined file')

    parser.add_argument('-f', '--format', type=str,
                        help='Specify a file format. None is default')

    parser.add_argument('--infiles', nargs='*',
                        help='file(s) to process')


    parser.add_argument('file', type=str,
                        help='first file to interleave or combined file to deinterleave')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='make it wordy')
    args = parser.parse_args()
    print(args)

    if args.format == 'neogeo':
        formatter = NeoGeo()
    else:
        formatter = None

    # if args.infiles:
    #     print(type(formatter))
    #     formatter.interleave_files(args.infiles)
    # else:
    #     print(type(formatter))

    if args.interleave:
        formatter.interleave_files(args.file, verbose=args.verbose)
    elif args.deinterleave:
        formatter.deinterleave_file(args.file, verbose=args.verbose)
    else:
        print('no operation selected')

