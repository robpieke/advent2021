with open('data/11.txt') as f:
    data = f.read().splitlines()

data = [[int(c) for c in d] for d in data]

blinks = 0

def advance(data, x, y, mx, my):
    blinks = 0
    if data[y][x] != -1:
        data[y][x] += 1
        if data[y][x] == 10:
            data[y][x] = -1
            blinks += 1
            if x > 0:
                blinks += advance(data, x-1, y, mx, my)
                if y > 0:
                    blinks += advance(data, x-1, y-1, mx, my)
                if y < my-1:
                    blinks += advance(data, x-1, y+1, mx, my)
            if y > 0:
                blinks += advance(data, x, y-1, mx, my)
            if x < mx-1:
                blinks += advance(data, x+1, y, mx, my)
                if y > 0:
                    blinks += advance(data, x+1, y-1, mx, my)
                if y < my-1:
                    blinks += advance(data, x+1, y+1, mx, my)
            if y < mx-1:
                blinks += advance(data, x, y+1, mx, my)
    return blinks

mx = len(data[0])
my = len(data)
for gen in range(100):
    for x in range(mx):
        for y in range(my):
            blinks += advance(data, x, y, mx, my)
    for x in range(mx):
        for y in range(my):
            data[y][x] = max(0, data[y][x])

print(blinks)