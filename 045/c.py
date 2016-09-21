def rec(S, i):
    if len(S) < i+1:
        return [S]
    # add + dont add
    return rec(S[:i] + "+" + S[i:], i+2) + rec(S, i+1) + [S[:i] + "+" + S[i:], S]


S = raw_input()
print sum([eval(s) for s in list(set(rec(S, 1)))])
