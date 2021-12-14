with open('data/04.txt') as f:
    data = f.read().splitlines()

numbers = [int(x) for x in data[0].split(',')]
boards = []

for i in range(2, len(data), 6):
    boards.append([int(x) for d in data[i:i+5] for x in d.split()])

bmasks = [2**26-1] * len(boards)

winners = [0]*10
for i in range(5):
    for j in range(5):
        winners[i] += 2**(i*5+j)
        winners[i+5] += 2**(i+j*5)

won = False
for n in numbers:
    for bi, b in enumerate(boards):
        for si, s in enumerate(b):
            if s == n:
                bmasks[bi] -= 2**si
                break
        for w in winners:
            if bmasks[bi] & w == 0:
                m = 0
                for i in range(25):
                    if bmasks[bi] & 2**i:
                        m += boards[bi][i]
                print(m*n)
                won = True
                break
    if won:
        break
