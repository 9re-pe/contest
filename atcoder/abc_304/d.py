from collections import defaultdict
from bisect import bisect


w, h = map(int, input().split())
n = int(input())
strawberries = []
for _ in range(n):
    p, q = map(int, input().split())
    strawberries.append((p, q))
n_a = int(input())
a = list(map(int, input().split()))
a.append(w)
n_b = int(input())
b = list(map(int, input().split()))
b.append(h)

strawberry_pieces = defaultdict(int)
maximum = 0
minimum = n
for strawberry in strawberries:
    p, q = strawberry
    ax = a[bisect(a, p)]
    bx = b[bisect(b, q)]
    strawberry_pieces[(ax, bx)] += 1
    maximum = max(maximum, strawberry_pieces[(ax, bx)])
    minimum = min(minimum, strawberry_pieces[(ax, bx)])

n_strawberry_piece = 0
num_li = []
for num in strawberry_pieces.values():
    n_strawberry_piece += 1
    num_li.append(num)

maximum = max(num_li)
minimum = min(num_li)

if n_strawberry_piece < (n_a + 1) * (n_b + 1):
    minimum = 0

print(minimum, maximum)
