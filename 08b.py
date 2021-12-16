with open('data/08.txt') as f:
    data = f.read().splitlines()

t = 0

for d in data:
    din, dout = d.split(' | ')
    digits = ['']*10
    # find 1, 4, 7, 8
    for w in din.split():
        if len(w) == 2:
            digits[1] = w
        elif len(w) == 3:
            digits[7] = w
        elif len(w) == 4:
            digits[4] = w
        elif len(w) == 7:
            digits[8] = w
    # find 9 and 3
    for w in din.split():
        if w in digits:
            continue
        if len(w) == 6:
            if all([x in w for x in digits[4]]):
                digits[9] = w
        elif len(w) == 5:
            if all([x in w for x in digits[7]]):
                digits[3] = w
    # find 5 and 6
    for w in din.split():
        if w in digits:
            continue
        if len(w) == 6:
            for w2 in din.split():
                if w2 in digits:
                    continue
                if len(w2) == 5:
                    if all([x in w for x in w2]):
                        digits[5] = w2
                        digits[6] = w
    # find 2 and 0
    for w in din.split():
        if w in digits:
            continue
        if len(w) == 5:
            digits[2] = w
        elif len(w) == 6:
            digits[0] = w

    dmap = {}
    for i in range(10):
        dmap[str(sorted(digits[i]))] = i

    n = 0
    for w in dout.split():
        n *= 10
        n += dmap[str(sorted(w))]

    t += n

print(t)
