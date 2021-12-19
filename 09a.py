with open('data/09.txt') as f:
    data = f.read().splitlines()

data = [[int(x) for x in d] for d in data]

risk = 0

for y in range(len(data)):
    for x in range(len(data[0])):
        if (x>0              and data[y][x]>=data[y][x-1]) or \
           (x<len(data[0])-1 and data[y][x]>=data[y][x+1]) or \
           (y>0              and data[y][x]>=data[y-1][x]) or \
           (y<len(data)-1    and data[y][x]>=data[y+1][x]):
            continue
        risk += 1+data[y][x]

print(risk)