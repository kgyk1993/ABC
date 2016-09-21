n, q = map(int, raw_input().split())
ban = [0 for i in range(n+1)]
res = [0 for i in range(n+1)]
for i in range(q):
    a, b = map(int, raw_input().split())
    ban[a-1] += 1
    ban[b] -= 1

tmp = 0
for i in range(n+1):
    tmp += ban[i]
    res[i] = tmp % 2
print "".join([str(ele) for ele in res[:-1]])
