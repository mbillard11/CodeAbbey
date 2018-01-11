cases = int(raw_input())
numbers = map(int, raw_input().split())

for i in numbers:
    count = 0
    while (i != 1):
        if i%2 == 0:
            i = i/2
        else:
            i = i*3 + 1
        count = count + 1
    print count,
    

