tot_lines = int(raw_input())

for i in range(0, tot_lines):   
    line = raw_input()
    num = map(int, line.split())
    sort = sorted(num)
    a = sort[0]
    b = sort[1]
    c = sort[2]
    if (a + b > c):
        print 1, 
    else:
        print 0,
