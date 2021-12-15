with open('data/06.txt') as f:
    data = f.read()

t = 0

for d in data.split(','):
    f = [int(d)]
    for i in range(80):
        for j in range(len(f)):
            if f[j] == 0:
                f[j] = 6
                f.append(8)
            else:
                f[j] -= 1
    t += len(f)

print(t)