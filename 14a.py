with open('data/14.txt') as f:
    data = f.read().splitlines()

state = data[0]

rules = {}

for d in data[2:]:
    k,v = d.split(' -> ')
    rules[k] = v

for step in range(10):
    nxt = state[0]
    for i in range(len(state)-1):
        k = state[i:i+2]
        nxt += rules[k]
        nxt += k[1]
    state = nxt

import string

cnts = list(filter(lambda x: x != 0, sorted([state.count(k) for k in string.ascii_uppercase])))

print(cnts[-1]-cnts[0])

