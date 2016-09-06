n = int(raw_input())
k = int(raw_input())
x = int(raw_input())
y = int(raw_input())

if n <= k:
    print x * n
else:
    print x * k + y * (n-k)
