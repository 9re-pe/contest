"""
再帰DFS->TLE
ルートの保存方式を変えてもダメ(むしろ遅くなる)
"""


from collections import deque
import sys
sys.setrecursionlimit(10**9)


def dfs(u):
    global visited
    global prev

    if visited[u]:
        return

    visited[u] = True

    for v in graph[u]:
        if visited[v]:
            continue
        prev[v] = u
        dfs(v)


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
prev = [-1] * n

dfs(x)
ans = []
cur = y
while cur != -1:
    ans.append(cur+1)  # 1インデントにする
    cur = prev[cur]
ans.reverse()
print(*ans)
