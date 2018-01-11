infoStr = raw_input()
info = map(int, infoStr.split())
m = info[0]
n = info[1]
count = [0]*n

valuesStr = raw_input()
values = map(int, valuesStr.split())

for x in values:
    count[x-1] = count[x-1] + 1

for i in count:
    print i,