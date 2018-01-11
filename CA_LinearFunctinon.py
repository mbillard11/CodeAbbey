cases = int(raw_input())

for x in range(0, cases):
    numbers = map(int, raw_input().split())
    x1, y1, x2, y2 = numbers
    a = ((y2 - y1) / (x2 - x1))
    b = y1 - (a*x1)
    print "("
    print a, b
    print ")",