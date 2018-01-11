array = map(float, raw_input().split())

# For Passes #

swaps = 0
didSwap = True
i = 0
j = 0

while didSwap == True:
    for x in range(0, len(array)-1):
        if array[x+1] != -1:
            i = array[x]
            j = array[x+1]
            if j<i:
                array[x] = j
                array[x+1] = i
                swaps = swaps + 1
                didSwap = False

# For Checksum #

result = 0                                                  #Checksum
seed = 113
modulo = 10000007

for num in array[:-1]:
    result = ((result + num)*seed) % modulo 

print swaps, int(result)


1 4 3 2 6 5 -1
1 3 4 2 6 5
1 3 2 4 6 5
1 3 2 4 5 6
