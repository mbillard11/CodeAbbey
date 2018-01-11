cases = int(raw_input())

temps = map(float, raw_input().split())
tempsNew = [0]*cases

tempsNew[0] = temps[0]
tempsNew[-1] = temps[-1]

print tempsNew[0],

for x in range(1, cases-1):
    tempsNew[x] = (temps[x-1] + temps[x] + temps[x+1]) / 3
    print tempsNew[x],
    
print tempsNew[-1]


