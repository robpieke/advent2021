with open('data/01.txt') as f:
    dn = [int(d) for d in f.read().splitlines()]

inc = 0
for i in range(1, len(dn)-2):
    if dn[i+2] > dn[i-1]:
        inc += 1
print(inc)