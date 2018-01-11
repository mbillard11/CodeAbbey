tot_lines = int(raw_input())

for i in range(0, tot_lines):
    line = raw_input()
    num = map(float, line.split())
    base = num[0]
    incr = num[1]
    steps = num[2]
    total = 0


    for x in steps:
        total = base + incr*x
        stepSum = stepSum + total

    print total,