m = int(raw_input())
res = 0

if m < 100:
    res = 0
elif 100 <= m <= 5000:
    res = m / 100.0
elif 6000 <= m <= 30000:
    res = m / 1000.0 + 50
elif 35000 <= m <= 70000:
    res = m / 1000.0 - 30
    res = res / 5 + 80
elif m > 70000:
    res = 89

print "%02.0f" % res
