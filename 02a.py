with open('data/02.txt') as f:
    data = f.read().splitlines()

x=0
y=0

for d in data:
    k,v = d.split(' ')
    if k == 'up':
        y -= int(v)
    elif k == 'down':
        y += int(v)
    else:
        x += int(v)

print(x*y)
