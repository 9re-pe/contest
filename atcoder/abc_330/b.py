n, l, r = map(int, input().split())
a = list(map(int, input().split()))

x = []
for ai in a:
    if ai < l:
        x.append(l)
    elif ai > r:
        x.append(r)
    else:
        x.append(ai)

print(*x)
