from struct import Struct

#all i ask for is "interleave {files here} bytesize" 
#and the opposite "deinterleave interleavedfile bytesize numberoffiles"
#example midway unit T
#functions should accept a list, and numbytes to (de)interleave by

def deinterleave(data, nbytes, nsplit):
    """Deinterleaves one bytearray into nsplit many bytearrays on a nbytes basis.

    Returns a list of bytearrays.
    """
    deinterleaved = [[] for n in range(nsplit)]

    deinterleave_s = Struct('c' * nbytes)
    deinterleave_iter = deinterleave_s.iter_unpack(data)

    for i in deinterleave_iter:
        deinterleaved[0].extend([*i])
        for j in range(1, len(deinterleaved[1:]) + 1):
            next_ = next(deinterleave_iter)
            deinterleaved[j].extend([*next_])

    return [b''.join(delist) for delist in deinterleaved]

def interleave(data, nbytes):
    """Interleaves a list of bytearrays together on a nbytes basis.

    Returns a bytearray.
    """
    interleave_s = Struct('c' * nbytes)
    iters = [interleave_s.iter_unpack(inter) for inter in data]

    interleaved = []
    #this could cause rounding errors?
    iterlen = int(len(data[0]) / nbytes)
    for i in range(iterlen):
        nexts = [next(iter_) for iter_ in iters]
        # print('nexts is:', nexts)
        interleaved.extend([b''.join(val) for val in nexts])
        # print('interleaved is:', interleaved)

    return b''.join(interleaved)

if __name__ == '__main__':
    data1 = bytearray.fromhex('AA AA AA AA BB BB BB BB CC CC CC CC DD DD DD DD')
    result = deinterleave(data1, 1, 8)
    #print(result)
    #newresult = interleave(result, 2)
    #print(newresult)

