raw_input()
a = map(int, raw_input().split())
res = 10**9+7
for i in range(min(a), max(a)+1):
    tmp = sum([(i-x)**2 for x in a])
    if tmp < res:
        res = tmp
print res
