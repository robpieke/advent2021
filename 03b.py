with open('data/03.txt') as f:
    data = f.read().splitlines()

import operator

def filterdata(data, op):
    fdata = data.copy()
    for i in range(len(data[0])):
        if len(fdata) == 1:
            break
        cnt = [d[i] == '1' for d in fdata].count(True)
        if op(cnt, len(fdata)/2):
            fdata = list(filter(lambda row: row[i] == '1', fdata))
        else:
            fdata = list(filter(lambda row: row[i] == '0', fdata))
    return int(fdata[0], 2)

print(filterdata(data, operator.ge) * filterdata(data, operator.lt))
