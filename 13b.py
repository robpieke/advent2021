with open('data/13.txt') as f:
    data = f.read().splitlines()

split = data.index('')
dots = []
for i in range(split):
    x,y = data[i].split(',')
    dots.append((int(x), int(y)))

folds = []
for i in range(split+1, len(data)):
    fold = data[i].split()[-1]
    axis,n = fold.split('=')
    folds.append((axis, int(n)))

for fa, fn in folds:
    for i in range(len(dots)):
        if fa == 'x' and dots[i][0] > fn:
            dots[i] = (2*fn-dots[i][0], dots[i][1])
        elif fa == 'y' and dots[i][1] > fn:
            dots[i] = (dots[i][0], 2*fn-dots[i][1])

dots = sorted(list(set(dots)), key=lambda x: x[1]*1000+x[0])

code = ''
x = -1
y = 0

for dot in dots:
    if dot[1] != y:
        code += '\n'
        x = 0
        y += 1
    code += '  '*(dot[0]-x-1)
    code += '**'
    x = dot[0]

print(code)