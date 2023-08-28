from collections import deque

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
prev = [-1] * n  # 各ノードの前のノードを保存するためのリスト

stack = deque()
stack.append(x)
while stack:
    u = stack.pop()
    if visited[u]:
        continue
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            prev[v] = u
            stack.append(v)

# xからyまでのパスを構築
path = []
curr = y
while curr != -1:
    path.append(curr + 1)  # 1インデックスに戻す
    curr = prev[curr]
path.reverse()

print(*path)
