def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n - 1, n + s)

recurse(4, 3)
recurse(-1, 0)