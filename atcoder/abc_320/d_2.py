import sys

LIMIT = 10**6
sys.setrecursionlimit(LIMIT)


def dfs(u):
    if visited[u]:
        return

    visited[u] = True

    for v in graph[u]:
        pos[v] = (pos[u][0] + diff[(u, v)][0], pos[u][1] + diff[(u, v)][1])
        dfs(v)


n, m = map(int, input().split())

graph = [[] for _ in range(n)]
diff = {}
for _ in range(m):
    a, b, x, y = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)
    diff[(a, b)] = (x, y)
    diff[(b, a)] = (-x, -y)

visited = [False] * n
pos = [(0, 0)] * n

dfs(0)
for i in range(n):
    if visited[i]:
        print(*pos[i])
    else:
        print('undecidable')
