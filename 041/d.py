import itertools

N, M = map(int, raw_input().split())
Ms = []
for i in xrange(M):
    Ms.append(tuple(map(int, raw_input().split())))

res = 0
for ele in list(itertools.permutations(range(1, N+1))):
    rl = []
    for i in range(N):
        for j in range(i+1, N):
            rl.append((ele[i], ele[j]))
    rl = set(rl)
    flag = True
    for xx in Ms:
        if xx not in rl:
            flag = False
    if flag:
        res += 1

print res
