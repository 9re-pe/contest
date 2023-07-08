from collections import deque

# 入力
h, w = map(int, input().split())
grid = [list(input()) for _ in range(h)]

# グリッドを有効グラフに変換(隣接リスト表現)
n = h*w  # ノード数
graph = [[] for _ in range(n)]
for i in range(h):
    for j in range(w):
        # 現在地の文字列を取得
        cur = grid[i][j]
        # グラフ構造における番号
        cur_node = w * i + j

        if cur == 's':
            nxt = 'n'
        elif cur == 'n':
            nxt = 'u'
        elif cur == 'u':
            nxt = 'k'
        elif cur == 'k':
            nxt = 'e'
        elif cur == 'e':
            nxt = 's'
        else:
            nxt = 'none'

        # 周囲4箇所に関してエッジを張れたら張る
        if i+1 < h and grid[i+1][j] == nxt:
            tmp = cur_node + w
            graph[cur_node].append(tmp)
        if i-1 >= 0 and grid[i-1][j] == nxt:
            tmp = cur_node - w
            graph[cur_node].append(tmp)
        if j+1 < w and grid[i][j+1] == nxt:
            tmp = cur_node + 1
            graph[cur_node].append(tmp)
        if j-1 >= 0 and grid[i][j-1] == nxt:
            tmp = cur_node - 1
            graph[cur_node].append(tmp)

# print(*graph)

# キューの用意
que = deque()

# 訪問済みを管理するリスト
visited = [False] * n

# 距離を管理するリスト
d = [-1] * n

# 始点の設定
s = 0
visited[0] = True

# 幅優先探索
que.append(s)
d[s] = 0
while que:
    # uをキューから取り出す
    u = que.popleft()

    for v in graph[u]:
        # 訪問済みであればスキップ
        if visited[v]:
            continue
        # 距離を計算
        d[v] = d[u] + 1
        # 訪問済みにする
        visited[v] = True
        # キューに入れる
        que.append(v)

# print(*d)

# 始点がsでない場合
if grid[0][0] != 's':
    print('No')

elif d[n-1] == -1:
    print('No')
else:
    print('Yes')
