cases = int(raw_input())

for i in range(0, cases):
    winsA = 0
    winsB = 0
    info = raw_input().split()
    for x in info:
        a,b = x
        if a == b:
            pass
        elif a == 'R':
            if b == 'P':
                winsB += 1
            else:
                winsA += 1
        elif a == 'P':
            if b == 'S':
                winsB += 1
            else:
                winsA += 1            
        elif a == 'S':
            if b == 'R':
                winsB += 1
            else:
                winsA += 1   
    if winsA>winsB:
        print '1',
    else:
        print '2',