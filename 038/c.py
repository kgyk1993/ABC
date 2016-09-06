raw_input()
a = map(int, raw_input().split())
b = [0]
res = [1]
for i, e in enumerate(a):
    if i != 0:
        if a[i-1] < a[i]:
            b.append(b[-1] + 1)
            res.append(b[-1] + 1 + res[-1])
        else:
            b.append(0)
            res.append(b[-1] + 1 + res[-1])
print res.pop()
