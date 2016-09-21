from collections import Counter

s = list(raw_input())
t = int(raw_input())

c = Counter(s)
now = abs(c["U"] - c["D"]) + abs(c["R"] - c["L"])
if t == 1:
    print now + c["?"]
else:
    now -= c["?"]
    if now > 0:
        print now
    else:
        if now % 2 == 0:
            print 0
        else:
            print 1
