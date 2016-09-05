s = raw_input()
ans = []
for ele in s:
    if ele != "B":
        ans.append(ele)
    else:
        try:
            ans.pop()
        except:
            pass
print "".join(ans)
