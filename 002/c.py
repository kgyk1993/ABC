import math

x1, y1, x2, y2, x3, y3 = map(int, raw_input().split())
print math.fabs(x1*y2 + x2*y3 + x3*y1 - y1*x2 - y2*x3 - y3*x1) / 2.0
