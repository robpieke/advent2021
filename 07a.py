with open('data/07.txt') as f:
    data = f.read()

import statistics

n = [int(d) for d in data.split(',')]
m = int(statistics.median(n))
f = sum([abs(d-m) for d in n])
print(f)
