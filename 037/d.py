res = []
h = w = 0
orig = []

def update(i, j):
    global res
    now = orig[i][j]
    if res[i][j] != 0:
        return res[i][j]
    ret = 0
    # left
    if i != 0:
        if orig[i-1][j] > now:
            ret += update(i-1, j)
    # right
    if i != h-1:
        if orig[i+1 if i != h-1 else i][j] > now:
            ret += update(i+1, j)
    # up
    if j != 0:
        if orig[i][j-1 if j != 0 else j] > now:
            ret += update(i, j-1)
    # down
    if j != w-1:
        if orig[i][j+1 if j != w-1 else j] > now:
            ret += update(i, j+1)

    res[i][j] = ret + 1
    return ret + 1


def main():
    global h, w, orig
    h, w = map(int, raw_input().split())
    targ = 0
    for i in range(h):
        x = map(int, raw_input().split())
        if targ < max(x):
            targ = max(x)
        orig.append(x)
    global res
    res = [[0 for i in range(w)] for j in range(h)]

    for i in range(h):
        for j in range(w):
            if res[i][j] == 0:
                res[i][j] = update(i, j)

    print sum([sum(ele) for ele in res])


if __name__ == "__main__":
    main()
