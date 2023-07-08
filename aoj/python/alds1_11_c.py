from collections import deque

# 入力
n = int(input())
graph = [[0]*n for _ in range(n)]
for _ in range(n):
    u, k, *v_list = map(int, input().split())
    # 0オリジン化
    u -= 1
    for v in v_list:
        # 0オリジン化
        v -= 1
        graph[u][v] = 1

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

    for v in range(n):
        # 繋がっていなければスキップ
        if graph[u][v] == 0:
            continue
        # 訪問済みであればスキップ
        if visited[v]:
            continue
        # 距離を計算
        d[v] = d[u] + 1
        # 訪問済みにする
        visited[v] = True
        # キューに入れる
        que.append(v)

# 出力
for i in range(n):
    print('{} {}'.format(i+1, d[i]))