from collections import deque

n, d = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(n)]

graph = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if (xy[i][0] - xy[j][0])**2 + (xy[i][1] - xy[j][1])**2 <= d**2:
            graph[i][j] = 1

que = deque()

visited = [False] * n

s = 0
visited[s] = True
que.append(s)

while que:
    u = que.popleft()

    for v in range(n):
        if graph[u][v] == 0:
            continue
        if visited[v]:
            continue

        visited[v] = True
        que.append(v)

for i in range(n):
    if visited[i]:
        print('Yes')
    else:
        print('No')
