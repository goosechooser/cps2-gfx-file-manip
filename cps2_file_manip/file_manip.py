import sys
import struct
#all i ask for is "interleave {files here} bytesize"
#and the opposite "deinterleave interleavedfile bytesize numberoffiles"
#example midway unit T
#functions should accept a list, and numbytes to (de)interleave by

def deinterleave(data, nbytes, nsplit):
    """Deinterleaves one bytearray into nsplit many bytearrays on a nbytes basis.

    Returns a list of bytearrays.
    """
    deinterleaved = [[] for n in range(nsplit)]

    deinterleave_s = struct.Struct('c' * nbytes)

    try:
        deinterleave_iter = deinterleave_s.iter_unpack(data)
    except struct.error as error:
        print('ERROR:', error, 'CLOSING', file=sys.stderr)
        sys.exit(1)

    #this could cause rounding errors?
    iterlen = int(len(data) / (nbytes * nsplit))
    print('iterlen is:', iterlen)
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
