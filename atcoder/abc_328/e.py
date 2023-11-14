from itertools import combinations


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
        parent[root_x] = root_y
        return True
    return False


n, m, k = map(int, input().split())
edges = []
min_cost = 0
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))
    min_cost += w

parent = list(range(n))

for combination in combinations(edges, n - 1):
    cost, parent = 0, list(range(n))
    for u, v, w in combination:
        if union(u - 1, v - 1):
            cost += w

    if len(set(find(x) for x in range(n))) == 1:
        min_cost = min(min_cost, cost % k)

print(min_cost)
