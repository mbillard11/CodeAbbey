info = map(int, raw_input().split())

numOfPeople = info[0]
steps = info[1]

listOfPeople = [0]*numOfPeople

for x in range(0, numOfPeople):
    listOfPeople[x] = x+1

kills = 0
killPos = steps - 1


while (kills < numOfPeople - 1):
    while (killPos < len(listOfPeople)):
        listOfPeople.pop(killPos)
        kills += 1
        killPos += (steps - 1)
    killPos -= len(listOfPeople)

print listOfPeople[0]



1 2 3 4 5 6 7 8 9 10
len = 10
step = 3

1 2 4 5 7 8 10
len = 7
killPos = 8

1 4 5 8 10
len = 5
killPos = 5 > 0
kill = 5

