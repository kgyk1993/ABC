n = int(raw_input())

ans = 10**9 + 7
for i in xrange(int(n**0.5), 0, -1):
    x = n / i
    ans = min(ans, (n - i*x)+abs(i - x))
print int(ans)
