n, q = map(int, raw_input().split())
a = [0 for i in range(n)]
for i in range(q):
    l, r, t = map(int, raw_input().split())
    for j in range(l-1, r):
        a[j] = t

for ele in a:
    print ele
