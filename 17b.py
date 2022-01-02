with open('data/17.txt') as f:
    data = f.read()

y0, y1 = data.split(', y=')[1].split('..')
vy0 = int(y0)
vy1 = max(int(y1), -int(y0)-1)

import math

x0, x1 = data.split('target area: x=')[1].split(',')[0].split('..')
vx0 = int(math.ceil(-1 + math.sqrt(1 + 8*int(x0)) / 2))
vx1 = int(x1)

x0 = int(x0)
y0 = int(y0)
x1 = int(x1)
y1 = int(y1)

routes = 0

for vx in range(vx0, vx1+1):
    for vy in range(vy0, vy1+1):
        _vx = vx
        _vy = vy
        x=0
        y=0
        while x <= x1 and (y >= y0 or _vy > 0):
            x += _vx
            y += _vy
            _vx = max(0, _vx-1)
            _vy -= 1
            if x >= x0 and y >= y0 and x <= x1 and y <= y1:
                routes += 1
                break

print(routes)
