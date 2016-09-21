res = [0] * 290

N = int(raw_input())
for num in xrange(N):
    start, end = raw_input().split("-")
    sm = int(start[0:2]) * 60 + int(start[2:4])
    em = int(end[0:2]) * 60 + int(end[2:4])
    sm -= sm % 5
    if em % 5 != 0:
        em += 5 - (em % 5)
    sa = sm / 5
    ea = em / 5
    res[sa] += 1
    res[ea] -= 1

inrain = False
buff = ""
now = 0

for aa in xrange(290):
    now += res[aa]
    if inrain:
        if now == 0:
            x = aa * 5
            print buff + "{0:02d}".format(x / 60) + "{0:02d}".format(x % 60)
            inrain = False
    else:
        if now != 0:
            x = aa * 5
            buff = "{0:02d}".format(x / 60) + "{0:02d}".format(x % 60) + "-"
            inrain = True
