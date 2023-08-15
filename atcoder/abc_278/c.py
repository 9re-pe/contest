n, q = map(int, input().split())
f = set()

for _ in range(q):
    t, a, b = map(int, input().split())

    if t == 1:
        f.add((a, b))
    elif t == 2:
        if (a, b) in f:
            f.remove((a, b))
    else:
        if (a, b) in f and (b, a) in f:
            print('Yes')
        else:
            print('No')
