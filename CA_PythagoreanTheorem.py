cases = int(raw_input())

for x in range(0, cases): 
    tri = map(float, raw_input().split())
    a = tri[0]
    b = tri[1]
    c = tri[2]
    hyp = (a*a + b*b)**.5

    if (c == hyp):
        print 'R',
    elif (c > hyp):
        print 'O',
    elif (c < hyp):
        print 'A',
