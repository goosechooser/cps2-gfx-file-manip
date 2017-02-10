import sys
import struct

def deinterleave(data, nbytes, nsplit):
    """Deinterleaves one bytearray into nsplit many bytearrays on a nbytes basis.

    Returns a list of bytearrays.
    """
    deinterleaved = [[] for n in range(nsplit)]

    deinterleave_s = struct.Struct('c' * nbytes)

    try:
        deinterleave_iter = deinterleave_s.iter_unpack(data)
    except struct.error as error:
        #this error can be many things, handling generically until otherwise
        print('ERROR:', error, 'CLOSING', file=sys.stderr)
        sys.exit(1)

    #this could cause rounding errors?
    iterlen = int(len(data) / (nbytes * nsplit))
    #print('iterlen is:', iterlen)
    for _ in range(iterlen):
        for i, _ in enumerate(deinterleaved):
            try:
                next_ = next(deinterleave_iter)
            except StopIteration:
                pass
            deinterleaved[i].extend([*next_])

    return [b''.join(delist) for delist in deinterleaved]

def interleave(data, nbytes):
    """Interleaves a list of bytearrays together on a nbytes basis.

    Returns a bytearray.
    """
    interleave_s = struct.Struct('c' * nbytes)
    iters = []

    for inter in data:
        try:
            iters.append(interleave_s.iter_unpack(inter))
        except struct.error as error:
            print('ERROR:', error, 'CLOSING', file=sys.stderr)
            sys.exit(1)

    interleaved = []
    #this could cause rounding errors?
    iterlen = int(len(data[0]) / nbytes)
    for _ in range(iterlen):
        nexts = [next(iter_) for iter_ in iters]
        # print('nexts is:', nexts)
        interleaved.extend([b''.join(val) for val in nexts])
        # print('interleaved is:', interleaved)

    return b''.join(interleaved)

def swap(data, fmt):
    """Swaps byte order of given bytearray based on the format given.

    Returns a bytearray.
    """
    swap_fmt = ''.join(['>', fmt])

    try:
        swap_iter = struct.iter_unpack(fmt, data)
    except struct.error as error:
        print('ERROR:', error, 'CLOSING', file=sys.stderr)
        sys.exit(1)

    try:
        swapped = [struct.pack(swap_fmt, *i) for i in swap_iter]
    except struct.error as error:
        print('ERROR:', error, '\nswap_fmt is:', swap_fmt, 'CLOSING', file=sys.stderr)
        sys.exit(1)

    # print('swapped is:', swapped)
    return b''.join(swapped)
