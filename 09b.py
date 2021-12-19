with open('data/09.txt') as f:
    data = f.read().splitlines()

data = [[int(x) for x in d] for d in data]

def buildBasin(data, x, y, mask):
    if (x,y) in mask or data[y][x] == 9:
        return 0
    basin = 1
    mask.add((x,y))
    if x > 0:
        basin += buildBasin(data, x-1, y, mask)
    if y > 0:
        basin += buildBasin(data, x, y-1, mask)
    if x < len(data[0])-1:
        basin += buildBasin(data, x+1, y, mask)
    if y < len(data)-1:
        basin += buildBasin(data, x, y+1, mask)
    return basin

basins = []
mask = set()
for y in range(len(data)):
    for x in range(len(data[0])):
        basins.append(buildBasin(data, x, y, mask))

topbasins = sorted(basins, reverse=True)[0:3]
print(topbasins[0]*topbasins[1]*topbasins[2])