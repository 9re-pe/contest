def dfs(u):
    if visited[u]:
        return

    visited[u] = True

    for v in range(n):
        if graph[u][v] == (INF, INF):
            continue
        if visited[v]:
            continue
        pos[v] = [pos[u][0] + graph[u][v][0], pos[u][1] + graph[u][v][1]]
        dfs(v)


INF = 10**10
n, m = map(int, input().split())

graph = [[(INF, INF)] * n for _ in range(n)]
for _ in range(m):
    a, b, x, y = map(int, input().split())
    a -= 1
    b -= 1
    graph[a][b] = (x, y)
    graph[b][a] = (-x, -y)

visited = [False] * n
pos = [(0, 0)] * n

dfs(0)
for i in range(n):
    if visited[i]:
        print(*pos[i])
    else:
        print('undecidable')
