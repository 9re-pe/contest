from collections import defaultdict, deque


n = int(input())
a = [-1] + list(map(int, input().split()))

# 木の構築
tree = defaultdict(list)
for i in range(1, n+1):
    left = 2*i
    right = 2*i+1

    tree[a[i]].append(left)
    tree[a[i]].append(right)

# BFS
que = deque()
d = [-1] * (2*n+2)
s = 1
que.append(s)
d[s] = 0
while que:
    u = que.popleft()

    for v in tree[u]:
        d[v] = d[u] + 1
        que.append(v)

# 出力
for i in range(2*n+2):
    if i == 0:
        continue

    print(d[i])
