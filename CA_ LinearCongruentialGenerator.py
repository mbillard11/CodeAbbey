cases = int(raw_input())

for x in range(0, cases): 
    info = map(int, raw_input().split())
    a, c, m, x0, n = info
    xCur = x0
    xNext = 0

    for i in range(0, n):
        xNext = (((a * xCur) + c)) % m
        xCur = xNext
    
    print xCur,