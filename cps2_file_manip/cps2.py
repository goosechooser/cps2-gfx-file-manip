import os, sys
from . import file_manip

#GFX files (for cps2) seem to always be in batches of 4
#workflow along the lines of 
#point at first file (in batch of 4)
#grap the four files
#interleave the 4 in one go

def _format_fname(name, i):
    fsplit = name.split('.')
    basefname = fsplit[0]
    try:
        basefnum = int(fsplit[1][:-1])
    except IndexError:
        error = 'is an invalid file name. Files should be formatted as \'BASE.NUMBERm\''
        print(basefname, error, file=sys.stderr)
        sys.exit(1)

    fnum = ''.join([str(basefnum + (i * 2)), 'm'])
    fname = '.'.join([basefname, fnum])
    return fname

def _get_file_data(filepath):
    head, tail = os.path.split(filepath)

    to_split = []
    fnames = []

    for i in range(4):
        fname = _format_fname(tail, i)
        try:
            with open(os.path.join(head, fname), 'rb') as f:
                to_split.append(bytearray(f.read()))
        except FileNotFoundError as error:
            print(error, file=sys.stderr)
            sys.exit(1)

        fnames.append(fname)

    print('interleaving', *[name for name in fnames])
    return fnames, to_split

def _combine_file_names(fnames):
    fsplit = [os.path.split(name)[1] for name in fnames]
    base = fsplit[0].split('.')[0]
    fnums = [name.split(".")[-1] for name in fsplit]

    return '.'.join([base, *fnums, 'combined'])

def interleave_files(fname, verbose=False):
    """Interleaves a set of 4 cps2 graphics files."""

    names, to_split = _get_file_data(fname)
    interleaved = []

    split_data = [file_manip.deinterleave(fsplit, 2) for fsplit in to_split]
    data_iter = iter(split_data)

    for sdata in data_iter:
        next_data = next(data_iter)
        even = file_manip.interleave(sdata[0], next_data[0], 2)
        odd = file_manip.interleave(sdata[1], next_data[1], 2)
        interleaved.append((even, odd))

    inter_iter = iter(interleaved)

    second_interleave = []
    for i in inter_iter:
        next_data = next(inter_iter)
        second_interleave.append(file_manip.interleave(i[0], next_data[0], 64))
        second_interleave.append(file_manip.interleave(i[1], next_data[1], 64))

    final = file_manip.interleave(second_interleave[0], second_interleave[1], 1048576)

    head = os.path.split(fname)[0]
    comb_fname = _combine_file_names(names)

    if verbose:
        print("interleaved file", comb_fname, "created")

    with open(os.path.join(head, comb_fname), 'wb') as f:
        f.write(final)

def deinterleave_file(fname, verbose=False):
    """Deinterleaves a interleaved cps2 graphics file."""

    head, tail = os.path.split(fname)
    split_tail = tail.split('.')
    fnames = ['.'.join([split_tail[0], name]) for name in split_tail[1:-1]]

    try:
        with open(fname, 'rb') as f:
            data = bytearray(f.read())
    except FileNotFoundError as error:
        print(error, file=sys.stderr)
        sys.exit(1)

    print("deinterleaving", tail)

    first = file_manip.deinterleave(data, 1048576)

    second = []
    for half in first:
        second.extend(file_manip.deinterleave(half, 64))

    final = []
    for quarter in second:
        final.extend(file_manip.deinterleave(quarter, 2))

    deinterleaved = [file_manip.interleave(final[i], final[i+4], 2) for i in range(4)]

    for i, fname in enumerate(fnames):
        print("deinterleaved file", fname, "created")

        with open(os.path.join(head, fname), 'wb') as f:
            f.write(deinterleaved[i])