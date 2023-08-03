grid = [list(input()) for _ in range(8)]
i_map = [8, 7, 6, 5, 4, 3, 2, 1]
j_map = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

ans = (-1, -1)
for i in range(8):
    for j in range(8):
        if grid[i][j] == '*':
            ans = (i, j)

print(f'{j_map[ans[1]]}{i_map[ans[0]]}')

