with open('data/16.txt') as f:
    data = f.read()

data = bin(int(data, 16))[2:]

def parseNum(data):
    i = 0
    nb = ''
    while data[i] == '1':
        nb += data[i+1:i+5]
        i += 5
    nb += data[i + 1:i + 5]
    n = int(nb,2)
    return data[i+5:], n

import numpy

def parseData(data):
    v = int(data[0:3], 2)
    t = int(data[3:6], 2)
    if t == 4:
        data, n = parseNum(data[6:])
    else:
        sn = []
        o = int(data[6], 2)
        if o == 0:
            sl = int(data[7:22], 2)
            _data = data[22:22+sl]
            while _data:
                _data, n = parseData(_data)
                sn.append(n)
            data = data[22+sl:]
        else:
            ns = int(data[7:18], 2)
            data = data[18:]
            for i in range(ns):
                data, n = parseData(data)
                sn.append(n)
        if t == 0:
            n = numpy.sum(sn)
        elif t == 1:
            n = numpy.prod(sn)
        elif t == 2:
            n = numpy.min(sn)
        elif t == 3:
            n = numpy.max(sn)
        elif t == 5:
            n = 1 if sn[0] > sn[1] else 0
        elif t == 6:
            n = 1 if sn[0] < sn[1] else 0
        elif t == 7:
            n = 1 if sn[0] == sn[1] else 0

    return data, n

print(parseData(data)[1])