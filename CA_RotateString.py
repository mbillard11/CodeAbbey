cases = int(raw_input())

def rotate(string, amt):
    return string[-amt:] + string[:-amt]

for x in range(0, cases): 
    line = raw_input().split()
    amt = int(line[0])
    string = line[1]
    finLine = rotate(string, amt)
    print finLine,


#### OR ####

cases = int(raw_input())

def rotate(string, amt):
    return string[amt:] + string[:amt]

for x in range(0, cases): 
    line = raw_input().split()
    amt = int(line[0])
    string = line[1]
    finLine = rotate(string, amt)
    print finLine,