h, w = map(int, input().split())
grid = [list(input()) for _ in range(h)]

x = []
for j in range(w):
    cnt = 0
    for i in range(h):
        if grid[i][j] == '#':
            cnt += 1
    x.append(cnt)

print(*x)
