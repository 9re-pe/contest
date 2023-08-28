from itertools import combinations


n, m = map(int, input().split())
pairs = set()
for _ in range(m):
    k, *x = map(int, input().split())
    pairs |= set(combinations(x, 2))

if len(pairs) == n * (n-1) // 2:
    print('Yes')
else:
    print('No')
