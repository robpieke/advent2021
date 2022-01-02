with open('data/17.txt') as f:
    data = f.read()

y0, y1 = data.split(', y=')[1].split('..')
vy = max(int(y1), -int(y0)-1)

print(vy*(vy+1)//2)