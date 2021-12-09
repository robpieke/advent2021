with open('data/01.txt') as f:
    dn = [int(d) for d in f.read().splitlines()]

inc = 0
for i in range(1, len(dn)):
    if dn[i] > dn[i-1]:
        inc += 1
print(inc)