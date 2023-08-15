from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)


def dfs(u):
    global graph

    if u in visited:
        return

    visited.add(u)

    for v in graph[u]:
        dfs(v)


n = int(input())
# 次数0のノードは無視する
# ノード数Nより、次数1以上の頂点は高々2N
graph = defaultdict(list)
for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = set()

dfs(1)
print(max(visited))
