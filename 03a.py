with open('data/03.txt') as f:
    data = f.read().splitlines()

cnt = [0] * len(data[0])

for d in data:
    for i, c in enumerate(d):
        if c == '1':
            cnt[i] += 1

gamma = 0
epsilon = 0

for d in cnt:
    gamma *= 2
    epsilon *= 2
    if d > len(data)/2:
        gamma += 1
    else:
        epsilon += 1

print(gamma*epsilon)
