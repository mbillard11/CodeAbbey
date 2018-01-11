cases = int(raw_input())

for x in range(0, cases): 
    num = int(raw_input())
    a = 0
    b = 1
    index = 2
    val = a + b
    while num != val:
        a = b
        b = val
        val = a + b
        index += 1
    print index, 