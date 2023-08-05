import sys
sys.setrecursionlimit(10**6)


def dfs(now):
    visited[now] = True
    nodes = 1
    edges = 0
    for next_node, next_edge in graph[now]:
        # エッジを先に見る(ノードが訪問済みでもエッジが訪問済みとは限らない)
        if visited_edge[next_edge]:
            continue
        visited_edge[next_edge] = True
        edges += 1

        if not visited[next_node]:
            n, e = dfs(next_node)
            nodes += n
            edges += e

    # 連結成分のノード数とエッジ数を返す
    return nodes, edges


n, m = map(int, input().split())

# エッジの本数を数えやすいように隣接リスト表現
# エッジのカウントのためにエッジ番号iも追加
graph = [[] for _ in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append((v, i))
    graph[v].append((u, i))

visited = [False] * n
visited_edge = [False] * m

ans = 'Yes'
for i in range(n):
    # 未訪問のノードを始点にする
    if not visited[i]:
        nodes, edges = dfs(i)
        if nodes != edges:
            ans = 'No'
            break

print(ans)
