cases = int(raw_input())

info = map(int, raw_input().split())

for x in range(0, cases):
    count = 0
    num = info[x]
    binary = format(num if num >= 0 else (1 << 32) + num, '032b')
    for i in binary:
        if i != '0':
            count += 1
    print count,
