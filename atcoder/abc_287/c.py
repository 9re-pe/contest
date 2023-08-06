"""
TLE出たけど連結かどうかの判定を最後に持っていいったらACになった
"""

import sys
sys.setrecursionlimit(10**9)


def dfs(now):
    global graph
    global visited

    if visited[now]:
        return

    visited[now] = True

    for v in graph[now]:
        dfs(v)


n, m = map(int, input().split())

graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

# グラフが連結かどうか
visited = [False] * n
dfs(0)
if False in visited:
    print('No')
    exit(0)

# 閉路をもたない
if m >= n:
    print('No')
    exit(0)

# 全ての頂点の字数が2以下
# これがないとx型のグラフなどで失敗する
for i in range(n):
    if len(graph[i]) > 2:
        print('No')
        exit(0)

print('Yes')
