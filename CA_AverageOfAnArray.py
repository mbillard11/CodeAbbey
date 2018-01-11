tot_lines = int(raw_input())

for i in range(0, tot_lines):   
    line = raw_input()
    num = map(float, line.split())
    total = 0
    i = 0
    
    for x in num[:-1]:
        total = total + x
        i = i + 1
        
    avg = round(total/i)
    print int(avg), 