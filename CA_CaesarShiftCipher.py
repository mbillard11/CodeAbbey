info = map(int, raw_input().split())
lines, shift = info

for x in range(0, lines):
    line = raw_input()
    decode = [0]*len(line)
    for i in range(0, len(line)-1):
        if ord(line[i]) == 32:
            decode[i] = unichr(32)
        elif ord(line[i]) - shift < 65:
            decode[i] = unichr(ord(line[i]) + (26 - shift))
        else:
            decode[i] = unichr(ord(line[i]) - shift)
    for all in decode[:-1]:
        print all
    print '.',