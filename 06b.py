with open('data/06.txt') as f:
    data = f.read()

t = 0
known = {}
subknown = {}

for d in data.split(','):
    if int(d) in known:
        t += known[int(d)]
        continue
    subt = 0
    f = [int(d)]
    for i in range(128):
        for j in range(len(f)):
            if f[j] == 0:
                f[j] = 6
                f.append(8)
            else:
                f[j] -= 1
    for f_n in f:
        if f_n in subknown:
            subt += subknown[f_n]
            continue
        ff = [f_n]
        for i in range(128):
            for j in range(len(ff)):
                if ff[j] == 0:
                    ff[j] = 6
                    ff.append(8)
                else:
                    ff[j] -= 1
        subt += len(ff)
        subknown[f_n] = len(ff)
    known[int(d)] = subt
    t += subt

print(t)
