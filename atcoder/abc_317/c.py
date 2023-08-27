"""DFS"""


import sys
sys.setrecursionlimit(10**9)


def dfs(u, s):
    global ans

    visited[u] = True
    ans = max(ans, s)

    for v in range(n):
        if visited[v]:
            continue
        if graph[u][v] == 0:
            continue

        dfs(v, s+graph[u][v])

    # ロールバック
    visited[u] = False


n, m = map(int, input().split())
graph = [[0] * n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    graph[a][b] = c
    graph[b][a] = c

ans = 0
visited = [False] * n

for i in range(n):
    dfs(i, 0)

print(ans)
