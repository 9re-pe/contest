# UnionFindクラスは変更なし
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

# 修正されたコード
MOD = 998244353
h, w = 3, 3  # 例として3x3グリッドを使用
n = h * w
UF = UnionFind(n)

# グリッドのデータ（例として）
grid_data = [input() for _ in range(h)]

cnt = 0
green = [0] * n
for row in grid_data:
    for node in row:
        if node == '#':
            green[cnt] = 1
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cnt % w + dx, cnt // w + dy
                if 0 <= nx < w and 0 <= ny < h:
                    check = ny * w + nx
                    if green[check]:
                        UF.merge(cnt, check)
        cnt += 1

bunshi = 0
bunbo = 0
for i in range(h):
    for j in range(w):
        node = i * w + j
        if green[node]:
            continue  # 緑色のセルはスキップ

        bunbo += 1
        temp_uf = UnionFind(n)
        temp_uf.parent_size = UF.parent_size.copy()
        temp_uf.merge(node, node)  # 新しい緑色セルを追加

        # 新しいセルの周囲をチェック
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = j + dx, i + dy
            if 0 <= nx < w and 0 <= ny < h:
                check = ny * w + nx
                if green[check]:
                    temp_uf.merge(node, check)

        # 連結成分の数をカウント
        bunshi += len([x for x in temp_uf.parent_size if x < 0])

# 分母が0でないことを確認
if bunbo == 0:
    print("Error: Division by zero")
else:
    denominator = pow(bunbo, -1, MOD)
    print(bunshi * denominator % MOD)