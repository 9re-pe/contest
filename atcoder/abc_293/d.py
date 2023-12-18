# UnionFind
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


n, m = map(int, input().split())
UF = UnionFind(n)

cycle = 0
for _ in range(m):
    a, b, c, d = input().split()
    a = int(a)
    c = int(c)
    a -= 1
    c -= 1

    if UF.same(a, c):
        cycle += 1
    else:
        UF.merge(a, c)

n_group = len(UF.groups())
print(cycle, n_group - cycle)


