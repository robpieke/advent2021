with open('data/10.txt') as f:
    data = f.read().splitlines()

closers = { ')': 1, ']': 2, '}': 3, '>': 4 }
openers = { '(': ')', '[': ']', '{': '}', '<': '>' }

pts = []

stack = []
for d in data:
    for c in d:
        if c in openers:
            stack.append(openers[c])
        else:
            if stack[-1] != c:
                break
            stack.pop()
    if len(stack):
        lpts = 0
        for c in reversed(stack):
            lpts *= 5
            lpts += closers[c]
        pts.append(lpts)
    stack = []

print(sorted(pts)[len(pts)//2])