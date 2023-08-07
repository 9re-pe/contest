import sys
sys.setrecursionlimit(10**9)


def dfs(u):
    global graph
    global visited
    global cycle

    if visited[u] == 1:
        cycle = True
        return

    if visited[u] == 2:
        return

    # 訪問中マーク
    visited[u] = 1

    for v in graph[u]:
        dfs(v)

    # 訪問済みマーク
    visited[u] = 2


n = int(input())

edge_list = []
for _ in range(n):
    s, t = input().split()
    edge_list.append([s, t])

# node_idの割り当て
name2id = dict()
node_id = 0
for edge in edge_list:
    s = edge[0]
    t = edge[1]
    if s not in name2id:
        name2id[s] = node_id
        node_id += 1
    if t not in name2id:
        name2id[t] = node_id
        node_id += 1

# グラフの構築
graph = [[] for _ in range(len(name2id))]
for edge in edge_list:
    u = name2id[edge[0]]
    v = name2id[edge[1]]
    graph[u].append(v)
n_node = len(graph)
visited = [0] * n_node

cycle = False
for s in range(n_node):
    if visited[s] == 0:
        dfs(s)

if cycle:
    print('No')
else:
    print('Yes')
