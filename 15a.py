with open('data/15.txt') as f:
    data = f.read().splitlines()

cave = [[int(c) for c in r] for r in data]

csts = {}
for y in range(len(cave)):
    for x in range(len(cave[0])):
        csts[(x,y)] = 1000000000000000000000
csts[(0,0)] = 0

while True:
    k = min(csts, key=csts.get)
    cst = csts[k]
    x = k[0]
    y = k[1]
    if x == len(cave[0])-1 and y == len(cave)-1:
        print(cst)
        break
    if x > 0 and (x-1,y) in csts:
        csts[(x-1,y)] = min(csts[(x-1,y)], cst + cave[y][x-1])
    if x < len(cave[0])-1 and (x+1,y) in csts:
        csts[(x+1,y)] = min(csts[(x+1,y)], cst + cave[y][x+1])
    if y > 0 and (x,y-1) in csts:
        csts[(x,y-1)] = min(csts[(x,y-1)], cst + cave[y-1][x])
    if y < len(cave)-1 and (x,y+1) in csts:
        csts[(x,y+1)] = min(csts[(x,y+1)], cst + cave[y+1][x])
    csts.pop(k)