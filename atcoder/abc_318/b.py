n = int(input())
a = []
b = []
c = []
d = []
for _ in range(n):
    ai, bi, ci, di = map(int, input().split())
    a.append(ai)
    b.append(bi)
    c.append(ci)
    d.append(di)

b_max = max(b)
d_max = max(d)

grid = [[0] * b_max for _ in range(d_max)]
for i in range(n):
    for y in range(a[i], b[i]):
        for x in range(c[i], d[i]):
            grid[x][y] = 1

ans = 0
for row in grid:
    ans += sum(row)
print(ans)

