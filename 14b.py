with open('data/14.txt') as f:
    data = f.read().splitlines()

rules = {}

for d in data[2:]:
    k,v = d.split(' -> ')
    rules[k] = v

steps = 20

cnts = {}

for i,rule in enumerate(rules):
    state = rule
    for step in range(steps):
        nxt = state[0]
        for i in range(len(state)-1):
            k = state[i:i+2]
            nxt += rules[k]
            nxt += k[1]
        state = nxt
    cnt = {}
    for c in state[1:-1]:
        if not c in cnt:
            cnt[c] = 0
        cnt[c] += 1
    cnts[rule] = cnt

state = data[0]
for step in range(steps):
    nxt = state[0]
    for i in range(len(state) - 1):
        k = state[i:i + 2]
        nxt += rules[k]
        nxt += k[1]
    state = nxt

tcts = {}

for i in range(len(state)-1):
    k = state[i:i+2]
    if not k[0] in tcts:
        tcts[k[0]] = 0
    tcts[k[0]] += 1
    for ck in cnts[k]:
        if not ck in tcts:
            tcts[ck] = 0
        tcts[ck] += cnts[k][ck]
tcts[state[-1]] += 1

vals = sorted(list(tcts.values()))
print(vals[-1]-vals[0])