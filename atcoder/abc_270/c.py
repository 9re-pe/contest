"""再帰DFS->TLE"""


from collections import deque
import sys
sys.setrecursionlimit(10**9)


def dfs(u):
    global visited
    global flg
    global nodes

    if visited[u]:
        return

    visited[u] = True

    if not flg:
        nodes.append(u+1)  # 1インデックスに戻す

    if u == y:
        flg = True

    for v in graph[u]:
        if visited[v]:
            continue
        dfs(v)
        if not flg:
            nodes.pop()


n, x, y = map(int, input().split())
x -= 1
y -= 1

graph = [[] for _ in range(n)]
for _ in range(n-1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * n
flg = False
nodes = deque()

dfs(x)
print(*nodes)
