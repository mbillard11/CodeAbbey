value = int(raw_input())

line = raw_input().split()
op = line[0]
num = int(line[1])

while (op != '%'):
    if (op == '+'):
        value = value + num
    else:
        value = value * num
    line = raw_input().split()
    op = line[0]
    num = int(line[1])
value = value % num
print value
