cases = int(raw_input())

for i in range(0, cases):
    info = map(float, raw_input().split())
    x1, y1, x2, y2, x3, y3 = info
    line1 = ((x2-x1)**2 + (y2-y1)**2)**0.5
    line2 = ((x3-x1)**2 + (y3-y1)**2)**0.5
    line3 = ((x2-x3)**2 + (y2-y3)**2)**0.5
    s = (line1 + line2 + line3)/2
    area = (s*(s-line1)*(s-line2)*(s-line3))**0.5
    print area,