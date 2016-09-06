from itertools import combinations
N, A = map(int, raw_input().split())
x = map(int, raw_input().split())
res = 0
for i in range(1, N+1):
    for ele in combinations(x, i):
        if sum(ele)*1.0/i == A:
            res += 1
print res
# TLE
