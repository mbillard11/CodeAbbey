cases = int(raw_input())

values = map(int, raw_input().split())

for x in values:
    list = [x]
    y = ((x * x) / 100 ) % 10000
    steps = 1
    while y not in list:
        list.append(y)
        steps += 1
        y = ((y * y) / 100 ) % 10000
    print steps, 

