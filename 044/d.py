import sys


def calc(b, n):
    if n < b:
        return n
    else:
        return calc(b, n/b) + n % b


def main():
    n = int(raw_input())
    s = int(raw_input())
    if s == n:
        print n+1
    else:
        for b in xrange(2, int(n**(1./2))+1):
            if calc(b, n) == s:
                print b
                exit()
        for b in xrange(1, int(n**(1./2))+1):
            a = (n-s)/b + 1
            if calc(a, n) == s:
                print a
                exit()
        print -1


if __name__ == "__main__":
    # sys.setrecursionlimit(100*10000)
    main()
