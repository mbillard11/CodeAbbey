tot_lines = int(raw_input())

for i in range(0, tot_lines):
    line = raw_input()
    num = map(int, line.split())
    if (num[0]<num[1]<num[2] or num[2]<num[1]<num[0]):
        print num[1],
    elif (num[1]<num[0]<num[2] or num[2]<num[0]<num[1]):
        print num[0],
    else:
        print num[2],