n, k = map(int, raw_input().split())
a = map(int, raw_input().split())
mask = [0 for i in range(len(a))]
for i in range(k, len(a)+1):
    mask[i-k] += 1
    mask[i-1] += -1

tmp = 0
for i, e in enumerate(mask):
    if e == 0:
        mask[i] = k if tmp == k-1 else tmp
    elif e == 1:
        tmp += 1
        mask[i] = tmp
    else:
        mask[i] = tmp
        tmp -= 1
res = sum([a*b for a, b in zip(a, mask)])
print res
