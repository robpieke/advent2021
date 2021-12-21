with open('data/10.txt') as f:
    data = f.read().splitlines()

closers = { ')': 3, ']': 57, '}': 1197, '>': 25137 }
openers = { '(': ')', '[': ']', '{': '}', '<': '>' }

pts = 0

stack = []
for d in data:
    for c in d:
        if c in openers:
            stack.append(openers[c])
        else:
            if stack[-1] != c:
                pts += closers[c]
                break
            stack.pop()

print(pts)