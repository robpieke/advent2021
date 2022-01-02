with open('data/15.txt') as f:
    data = f.read().splitlines()

dx = len(data[0])
dy = len(data)

cave = []
for y in range(5*dy):
    r = []
    for x in range(5*dx):
        v = int((y//dy)+(x//dx)+int(data[y%dy][x%dx]))
        v = 1 + ((v-1)%9)
        r.append(v)
    cave.append(r)

csts = { (0,0): 0 }

dx = len(cave[0])
dy = len(cave)

def updateCost(csts, x, y, cst):
    if not (x,y) in csts:
        csts[(x,y)] = cst
    elif csts[(x,y)] != -1:
        csts[(x,y)] = min(csts[(x,y)], cst)

seen = set()

while True:
    k = min(csts, key=csts.get)
    cst = csts[k]
    x = k[0]
    y = k[1]
    if x == dx-1 and y == dy-1:
        print(cst)
        break
    if x > 0 and not (x-1,y) in seen:
        updateCost(csts, x-1, y, cst+cave[y][x-1])
    if y > 0 and not (x,y-1) in seen:
        updateCost(csts, x, y-1, cst+cave[y-1][x])
    if x < dx-1 and not (x+1,y) in seen:
        updateCost(csts, x+1, y, cst+cave[y][x+1])
    if y < dy-1 and not (x,y+1) in seen:
        updateCost(csts, x, y+1, cst+cave[y+1][x])
    csts.pop(k)
    seen.add(k)
