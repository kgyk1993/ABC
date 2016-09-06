h1, w1 = map(int, raw_input().split())
h2, w2 = map(int, raw_input().split())

if h1 == h2:
    print "YES"
elif h1 == w2:
    print "YES"
elif h2 == w1:
    print "YES"
elif w1 == w2:
    print "YES"
else:
    print "NO"
