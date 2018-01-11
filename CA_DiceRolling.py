tot_lines = int(raw_input())

for i in range(0, tot_lines):   
    line = raw_input()
    num = float(line)
    diceNum = int(num*6) + 1
    print diceNum,