cases = int(raw_input())

for x in range(0, cases):   

    line = map(float, raw_input().split())
    num = line[0]
    steps = int(line[1])

    r = 1

    for x in range(0, steps):
        r = (r + (num / r)) / 2

    print r,