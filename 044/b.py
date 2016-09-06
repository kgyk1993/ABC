from collections import Counter
w = list(raw_input())
c = Counter(w)
for k, v in c.items():
    if v % 2 == 1:
        print "No"
        exit()
else:
    print "Yes"
