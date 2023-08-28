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


def is_next(x1, y1, x2, y2):
    next_set = {
        (x1-1, y1-1),
        (x1-1, y1),
        (x1,   y1-1),
        (x1,   y1+1),
        (x1+1, y1),
        (x1+1, y1+1)
    }
    return (x2, y2) in next_set


n = int(input())
xy2i = {}
uf = UnionFind(n)
for i in range(n):
    x, y = map(int, input().split())
    xy2i[(x, y)] = i

    for xy in xy2i.keys():
        if is_next(x, y, xy[0], xy[1]):
            uf.merge(i, xy2i[(xy[0], xy[1])])

print(len(uf.groups()))
