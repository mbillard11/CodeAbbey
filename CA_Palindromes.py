cases = int(raw_input())

for x in range(0, cases): 
    line = raw_input()
    line = line.translate(None, ' !@#$,-')
    line = line.lower()
    line2 = line[::-1]
    if line == line2:
        print 'Y',
    else:
        print 'N',
