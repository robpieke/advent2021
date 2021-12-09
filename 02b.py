with open('data/02.txt') as f:
    data = f.read().splitlines()

x=0
y=0
aim=0

for d in data:
    k,v = d.split(' ')
    if k == 'up':
        aim -= int(v)
    elif k == 'down':
        aim += int(v)
    else:
        x += int(v)
        y += aim*int(v)

print(x*y)
