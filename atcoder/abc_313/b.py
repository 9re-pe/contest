n, m = map(int, input().split())
a = set()
b = set()
for _ in range(m):
    ai, bi = map(int, input().split())
    a.add(ai)
    b.add(bi)

candidates = a - b
if len(candidates) == 1:
    print(next(iter(candidates)))
else:
    print(-1)
