n, p, q = map(int, input().split())
d = list(map(int, input().split()))

mind = min(d)

if p < q + mind:
    print(p)
else:
    print(q + mind)
