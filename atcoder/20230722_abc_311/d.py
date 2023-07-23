import sys
sys.setrecursionlimit(10**6)


def dfs(i, j):
    global mt
    global visited
    global status

    print(i, j, status)
    visited[i][j] = 1

    if status == 'stop':
        if i-1 >= 0 and mt[i-1][j] == 0 and visited[i-1][j] == 0:
            status = 'up'
            dfs(i-1, j)
        if i+1 <= n-1 and mt[i+1][j] == 0 and visited[i+1][j] == 0:
            status = 'down'
            dfs(i+1, j)
        if j-1 >= 0 and mt[i][j-1] == 0 and visited[i][j-1] == 0:
            status = 'left'
            dfs(i, j-1)
        if j+1 <= m-1 and mt[i][j+1] == 0 and visited[i][j+1] == 0:
            status = 'right'
            dfs(i, j+1)
        return
    if status == 'up':
        if i-1 >= 0 and mt[i-1][j] == 0:
            dfs(i-1, j)
        else:
            status = 'stop'
            dfs(i, j)
    if status == 'down':
        if i+1 <= n-1 and mt[i+1][j] == 0:
            dfs(i+1, j)
        else:
            status = 'stop'
            dfs(i, j)
    if status == 'left':
        if j-1 >= 0 and mt[i][j-1] == 0:
            dfs(i, j-1)
        else:
            status = 'stop'
            dfs(i, j)
    if status == 'right':
        if j+1 <= m-1 and mt[i][j+1] == 0:
            dfs(i, j+1)
        else:
            status = 'stop'
            dfs(i, j)


n, m = map(int, input().split())
mt = [[0 for j in range(m)] for i in range(n)]
for i in range(n):
    s = list(input())
    for j in range(m):
        if s[j] == '#':
            mt[i][j] = 1

visited = [[0 for j in range(m)] for i in range(n)]
status = 'stop'
dfs(1, 1)

cnt = 0
for i in range(n):
    for j in range(m):
        if mt[i][j] == 0 and visited[i][j] == 1:
            cnt += 1
print(cnt)

# デバッグ用
for i in range(n):
    row = []
    for j in range(m):
        if mt[i][j] == 1:
            row.append('#')
        elif mt[i][j] == 0 and visited[i][j] == 1:
            row.append('x')
        else:
            row.append('.')
    print(''.join(map(str, row)))
