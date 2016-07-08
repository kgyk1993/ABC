raw_input()
a = [(i+1, ele) for i, ele in enumerate(map(int, raw_input().split()))]

for ele in sorted(a, key=lambda x: x[1], reverse=True):
    print ele[0]
