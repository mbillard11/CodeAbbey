cases = int(raw_input())

for x in range(0, cases): 
    info = map(int, raw_input().split())
    roll1, roll2 = info
    n = 6
    dice1 = roll1 % n
    dice1 += 1
    dice2 = roll2 % n
    dice2 += 1
    total = dice1 + dice2
    print total,