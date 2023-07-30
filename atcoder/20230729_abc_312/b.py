def is_tak_code(grid, i, j):
    # 左上
    for x in range(3):
        for y in range(3):
            if grid[i+x][j+y] != '#':
                return False
    for x in range(3):
        if grid[i+3][j+x] != '.':
            return False
    for x in range(3):
        if grid[i+x][j+3] != '.':
            return False
    if grid[i+3][j+3] != '.':
        return False

    # 右下
    for x in range(3):
        for y in range(3):
            if grid[i+6+x][j+6+y] != '#':
                return False
    for x in range(3):
        if grid[i+5][j+6+1] != '.':
            return False
    for x in range(3):
        if grid[i+6+x][j+5] != '.':
            return False
    if grid[i+5][j+5] != '.':
        return False

    return True


n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]
for i in range(n-8):
    for j in range(m-8):
        if is_tak_code(grid, i, j):
            print(i+1, j+1)
