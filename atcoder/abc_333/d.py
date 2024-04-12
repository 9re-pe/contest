"""
考え方
1. 1を削除するためには1が葉でなければならない
2. 1を削除する直前の状態では，1につながっている辺は1本しか残っていない状態
3. 1本残して，他の部分木を全て消さなければならない
4. 1につながっている部分木でどれを残すか -> 一番ノード数が多い木を残す

メモ: ノード数Nの部分木を消すのに必要な操作回数はN回
"""
import sys
sys.setrecursionlimit(10**9)


n = int(input())
graph = [[] for _ in range(n)]
for i in range(n-1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    if u != 0:
        graph[v].append(u)
visited = [False] * n


def dfs(u):
    global n_node

    if visited[u]:
        return

    visited[u] = True
    n_node += 1

    for v in graph[u]:
        dfs(v)


li_n_node = []
# 1の子ノードを始点とする
for s in graph[0]:
    n_node = 0
    dfs(s)
    li_n_node.append(n_node)

print(sum(li_n_node) - max(li_n_node) + 1)
