size = int(raw_input())

array = map(int, raw_input().split())
passes = 0
swaps = 0
didSwap = True
i = 0
j = 0
t = 0

while didSwap == True:
    didSwap = False
    for x in range (0, len(array)):
        if x+1 < len(array):
            i = array[x]
            j = array[x+1]
            if j<i:
                array[x] = j
                array[x+1] = i
                swaps = swaps + 1
                didSwap = True
    passes = passes + 1
print passes, swaps



3 1 4 1 5 9 2 6
1 3 1 4 5 2 6 9
1 1 3 4 2 5 6 9
1 1 3 2 4 5 6 9
1 1 2 3 4 5 6 9




1 546 7 4 2 324 768 4 123 456 6

line = raw_input().split()

print line
[1, 546, 7, 4, 2, .....]