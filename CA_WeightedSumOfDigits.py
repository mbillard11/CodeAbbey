tot_nums = int(raw_input())

line = raw_input()
nums = map(int, line.split())           #345 235 576567 234 123

for i in range(0, tot_nums):
    totalSum = 0
    count = 0
    number = nums[i]
    totStr = [int(d) for d in str(number)]  #[3,4,5]
    for x in totStr:
        count = count+1
        totalSum = totalSum + x*count
    print totalSum,