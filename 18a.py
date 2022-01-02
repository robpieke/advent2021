with open('data/18.txt') as f:
    data = f.read().splitlines()

import math

def parseLine(line):
    res = []
    d = 0
    for c in line:
        if c == '[':
            d += 1
        elif c == ']':
            d -= 1
        elif c == ',':
            pass
        else:
            res.append((int(c), d))
    return res

def reduceLine(line):
    while True:
        changed = False
        for i in range(len(line)):
            if line[i][1] == 5:
                if i != 0:
                    line[i-1] = (line[i-1][0] + line[i][0], line[i-1][1])
                if i != len(line)-2:
                    line[i+2] = (line[i+2][0] + line[i+1][0], line[i+2][1])
                line = line[0:i] + [(0, line[i][1]-1)] + line[i+2:]
                changed = True
                break
        if changed:
            continue
        for i in range(len(line)):
            if line[i][0] >= 10:
                line = line[0:i] + [(math.floor(line[i][0]/2.0), line[i][1]+1),
                                    (math.ceil(line[i][0]/2.0), line[i][1]+1)] + line[i+1:]
                changed = True
                break
        if changed:
            continue
        return line

def addLine(line1, line2):
    line = []
    for d in line1:
        line.append((d[0], d[1]+1))
    for d in line2:
        line.append((d[0], d[1]+1))
    return line

def scoreLine(line):
    while len(line) > 1:
        for i in range(len(line)-1):
            if line[i][1] == line[i+1][1]:
                line = line[0:i] + [(3*line[i][0] +
                                     2*line[i+1][0], line[i][1]-1)] + line[i+2:]
                break
    return line[0][0]

line = parseLine(data[0])
for d in data[1:]:
    line = addLine(line, parseLine(d))
    line = reduceLine(line)

print(scoreLine(line))