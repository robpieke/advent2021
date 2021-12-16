with open('data/08.txt') as f:
    data = f.read().splitlines()

t = 0

for d in data:
    din, dout = d.split(' | ')
    t += sum(len(w) <= 4 or len(w) == 7 for w in dout.split())

print(t)
