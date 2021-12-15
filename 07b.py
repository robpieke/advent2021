with open('data/07.txt') as f:
    data = f.read()

import statistics

n = [int(d) for d in data.split(',')]
m = int(statistics.median(n))

def cost(n, m):
    return sum([abs(d-m)*(abs(d-m)+1)//2 for d in n])

c = cost(n,m)

while True:
    c0 = cost(n,m-1)
    c1 = cost(n,m+1)
    if c0 < c:
        c = c0
        m -= 1
        continue
    elif c1 < c:
        c = c1
        m += 1
        continue
    break

print(c)