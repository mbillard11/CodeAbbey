cases = int(raw_input())

for x in range(0, cases): 
    info = map(float, raw_input().split())
    distance = info[0]
    speedA = info[1]
    speedB = info[2]
    time = distance / (speedA + speedB)
    disFromA = speedA*time
    print disFromA,