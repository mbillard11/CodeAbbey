size = int(raw_input())

array = map(int, raw_input().split())
posArray = [0]*size

for x in range(0, size):
    posArray[x] = x


didSwap = True
i = 0
j = 0
a = 0
b = 0


while didSwap == True:
    didSwap = False
    for x in range (0, size):
        if x+1 < len(array):
            i = array[x]
            a = posArray[x]
            j = array[x+1]
            b = posArray[x+1]
            if j<i:
                array[x] = j
                posArray[x] = b
                array[x+1] = i
                posArray[x+1] = a
                didSwap = True

for x in posArray:
    print x+1,
