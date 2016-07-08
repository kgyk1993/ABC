import math
N = int(raw_input())
a = map(int, raw_input().split())
a += [10000, 10000]

ans = [10**9+7 for i in xrange(len(a)+2)]
ans[0] = 0
for i in xrange(N):
    # single step
    tmp1 = ans[i] + math.fabs(a[i] - a[i+1])
    if tmp1 < ans[i+1]:
        ans[i+1] = tmp1
    # double step
    tmp2 = ans[i] + math.fabs(a[i] - a[i+2])
    if tmp2 < ans[i+2]:
        ans[i+2] = tmp2

print int(ans[N-1])
