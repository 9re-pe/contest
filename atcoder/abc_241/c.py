n = int(input())
grid = []
for _ in range(n):
    row = []
    s = input()
    for c in s:
        if c == '#':
            row.append(1)
        else:
            row.append(0)
    grid.append(row)

ans = 'No'
for i in range(n):
    for j in range(n):
        # 縦方向
        if i+5 <= n-1 and sum([grid[i+x][j] for x in range(6)]) >= 4:
            ans = 'Yes'
            break
        # 横方向
        if j+5 <= n-1 and sum(grid[i][j:j+6]) >= 4:
            ans = 'Yes'
            break
        # 斜め方向(右下)
        if i+5 <= n-1 and j+5 <= n-1 and sum([grid[i+x][j+x] for x in range(6)]) >= 4:
            ans = 'Yes'
            break
        # 斜め方向(左下)
        if i+5 <= n - 1 and j-5 >= 0 and sum([grid[i+x][j-x] for x in range(6)]) >= 4:
            ans = 'Yes'
            break

print(ans)
