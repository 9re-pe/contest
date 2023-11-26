import math


d = int(input())
INF = 10 ** 13
ans = INF
for x in range(int(math.sqrt(d)) + 1):
    y_square = d - x * x
    y = int(math.sqrt(y_square))
    if y * y == y_square:
        ans = 0
        break
    for dy in [-1, 0, 1]:
        y_adj = y + dy
        diff = abs(x * x + y_adj * y_adj - d)
        ans = min(ans, diff)
print(ans)
