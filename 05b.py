with open('data/05.txt') as f:
    data = f.read().splitlines()

cnt = 0
pts = {}

for d in data:
    s,e = d.split(' -> ')
    sx,sy = [int(x) for x in s.split(',')]
    ex,ey = [int(x) for x in e.split(',')]
    if sx > ex:
        dx = -1
    elif sx < ex:
        dx = 1
    else:
        dx = 0
    if sy > ey:
        dy = -1
    elif sy < ey:
        dy = 1
    else:
        dy = 0
    x=sx
    y=sy
    while x != ex+dx or y != ey+dy:
        if (x,y) in pts:
            if pts[(x,y)] == 1:
                cnt += 1
            pts[(x,y)] += 1
        else:
            pts[(x,y)] = 1
        x += dx
        y += dy

print(cnt)