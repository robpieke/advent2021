with open('data/16.txt') as f:
    data = f.read()

data = bin(int(data, 16))[2:]

def skipNum(data):
    i = 0
    while data[i] == '1':
        i += 5
    return data[i+5:]

def extractVersions(data):
    v = int(data[0:3], 2)
    t = int(data[3:6], 2)
    if t == 4:
        data = skipNum(data[6:])
    else:
        o = int(data[6], 2)
        if o == 0:
            sl = int(data[7:22], 2)
            _data = data[22:22+sl]
            while _data:
                _data, _v = extractVersions(_data)
                v += _v
            data = data[22+sl:]
        else:
            ns = int(data[7:18], 2)
            data = data[18:]
            for i in range(ns):
                data, _v = extractVersions(data)
                v += _v
    return data, v

print(extractVersions(data)[1])