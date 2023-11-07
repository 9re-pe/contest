class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent_size = [-1] * n

    def leader(self, a):
        if self.parent_size[a] < 0: return a
        self.parent_size[a] = self.leader(self.parent_size[a])
        return self.parent_size[a]

    def merge(self, a, b):
        x, y = self.leader(a), self.leader(b)
        if x == y: return
        if abs(self.parent_size[x]) < abs(self.parent_size[y]): x, y = y, x
        self.parent_size[x] += self.parent_size[y]
        self.parent_size[y] = x
        return

    def same(self, a, b):
        return self.leader(a) == self.leader(b)

    def size(self, a):
        return abs(self.parent_size[self.leader(a)])

    def groups(self):
        result = [[] for _ in range(self.n)]
        for i in range(self.n):
            result[self.leader(i)].append(i)
        return [r for r in result if r != []]


DIRECTIONS = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, 1),
    (0, -1),
    (1, 1),
    (1, 0),
    (1, -1),
]


h, w = map(int, input().split())
grid = [list(input()) for _ in range(h)]
node_id = dict()

cnt = 0
for i in range(h):
    for j in range(w):
        if grid[i][j] == '#':
            node_id[(i, j)] = cnt
            cnt += 1

UF = UnionFind(cnt)
for i in range(h):
    for j in range(w):

        if grid[i][j] == '.':
            continue

        for d in DIRECTIONS:
            next_i = i + d[0]
            next_j = j + d[1]
            if next_i < 0 or next_i >= h or next_j < 0 or next_j >= w:
                continue
            if grid[next_i][next_j] == '#':
                UF.merge(node_id[(i, j)], node_id[(next_i, next_j)])

print(len(UF.groups()))
