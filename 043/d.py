s = raw_input()
if len(s) == 2:
    if s[0] == s[1]:
        print "1 2"
        exit()

for i in range(len(s)-2):
    if len(set(s[i:i+2])) == 1:
        print i+1, i+2
        break
    elif len(set(s[i:i+3])) == 2:
        print i+1, i+3
        break
else:
    print "-1 -1"
