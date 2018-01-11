cases = int(raw_input())

for x in range(0, cases): 
    info = map(float, raw_input().split())
    deposit = info[0]
    goal =info[1]
    rate = info[2]
    account = deposit
    years = 0

    while account < goal:
        account = account + account*(rate / 100)
        account -= 0.005
        round(account, 2)
        years += 1

    print years,


121.3490398405