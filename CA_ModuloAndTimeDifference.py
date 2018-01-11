cases = int(raw_input())

for x in range(0, cases):
    times = map(int, raw_input().split())
    day1, hour1, min1, sec1, day2, hour2, min2, sec2  = times

    time1 = day1*86400 + hour1*3600 + min1*60 + sec1
    time2 = day2*86400 + hour2*3600 + min2*60 + sec2
    timeDiff = time2 - time1
    timeDiffDays = timeDiff / 86400
    timeDiffHours = (timeDiff % 86400) / 3600
    timeDiffMins = ((timeDiff % 86400) % 3600) / 60
    timeDiffSecs = (((timeDiff % 86400) % 3600) % 60

    print '('
    print timeDiffDays, timeDiffHours, timeDiffMins, timeDiffSecs
    print ')',