tot_lines = int(raw_input())

for i in range(0, tot_lines):
    line = raw_input()
    nums = map(int, line.split())
    total = nums[0]*nums[1]+nums[2]
    totStr = [int(d) for d in str(total)]
    finTot = 0
    for nums in totStr:
        finTot = finTot + nums
    print finTot, 