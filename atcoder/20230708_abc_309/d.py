from collections import deque

n1, n2, m = map(int, input().split())
graph = [[] for _ in range(n1+n2)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    # 無効グラフ
    graph[a].append(b)
    graph[b].append(a)

# グラフ1の探索---------------------------------------
que1 = deque()
visited1 = [False] * (n1+n2)
d1 = [-1] * (n1+n2)

# 始点の設定
s1 = 0
visited1[s1] = True

que1.append(s1)
d1[s1] = 0
while que1:
    # uをキューから取り出す
    u = que1.popleft()

    for v in graph[u]:
        if visited1[v]:
            continue
        d1[v] = d1[u] + 1
        visited1[v] = True
        que1.append(v)

# グラフ2の探索---------------------------------------
que2 = deque()
visited2 = [False] * (n1+n2)
d2 = [-1] * (n1+n2)

# 始点の設定
s2 = n1+n2-1
visited2[s2] = True

que2.append(s2)
d2[s2] = 0
while que2:
    u = que2.popleft()

    for v in graph[u]:
        if visited2[v]:
            continue
        d2[v] = d2[u] + 1
        visited2[v] = True
        que2.append(v)

print(max(d1) + max(d2) + 1)
