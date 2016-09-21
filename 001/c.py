deg, dis = map(int, raw_input().split())

a = [112.5, 337.5, 562.5, 787.5, 1012.5, 1237.5, 1462.5, 1687.5, 1912.5, 2137.5,
2362.5, 2587.5, 2812.5, 3037.5, 3262.5, 3487.5]
b = ["NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W",
"WNW", "NW", "NNW"]

di = "N"
for num in xrange(len(a) - 1):
    if a[num] <= deg:
        if a[num + 1] > deg:
            di = b[num]

c = [0.25, 1.55, 3.35, 5.45, 7.95, 10.75, 13.85, 17.15, 20.75, 24.45, 28.45, 32.65, 201]
dis = dis / 60.0

w = 0
for num in xrange(len(c) - 1):
    if c[num] <= dis:
        if a[num + 1] > dis:
            w = num + 1

if w == 0:
    di = "C"
print di + " " + str(w)
