with open('data/11.txt') as f:
    data = f.read().splitlines()

data = [[int(c) for c in d] for d in data]

def advance(data, x, y, mx, my):
    if data[y][x] != -1:
        data[y][x] += 1
        if data[y][x] == 10:
            data[y][x] = -1
            if x > 0:
                advance(data, x-1, y, mx, my)
                if y > 0:
                    advance(data, x-1, y-1, mx, my)
                if y < my-1:
                    advance(data, x-1, y+1, mx, my)
            if y > 0:
                advance(data, x, y-1, mx, my)
            if x < mx-1:
                advance(data, x+1, y, mx, my)
                if y > 0:
                    advance(data, x+1, y-1, mx, my)
                if y < my-1:
                    advance(data, x+1, y+1, mx, my)
            if y < mx-1:
                advance(data, x, y+1, mx, my)

mx = len(data[0])
my = len(data)
gen = 0
while(True):
    gen += 1
    for x in range(mx):
        for y in range(my):
            advance(data, x, y, mx, my)
    for x in range(mx):
        for y in range(my):
            data[y][x] = max(0, data[y][x])
    if sum([sum(r) for r in data]) == 0:
        break

print(gen)