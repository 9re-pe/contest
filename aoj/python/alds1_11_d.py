from collections import deque

# 入力(グラフの生成)
n, m = map(int, input().split())
# 隣接リスト
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    # 無効グラフ
    graph[u].append(v)
    graph[v].append(u)

# ラベル(どこの連結成分に属しているか)を管理するリスト
labels = [-1] * n

# 訪問済みを管理するリスト
visited = [False] * n

label = 0
# このループ1回でひとラベル分
while True:
    # キューの用意
    que = deque()

    # ラベルの生成
    label += 1

    # 始点の設定
    s = -1 # 判定用に値を持たせて初期化
    for i in range(n):
        # まだラベルが振られていないノードを探して始点にする
        if labels[i] == -1:
            s = i
            visited[s] = True
            que.append(s)
            labels[s] = label
            break

    # もうラベルが振られていないノードがなければ終了
    if s == -1:
        break

    # sを始点とする幅優先探索
    while que:
        # uをキューから取り出す
        u = que.popleft()

        # uからつながっている頂点を順に回る
        for v in graph[u]:
            # 訪問済みであればスキップ
            if visited[v]:
                continue
            # ラベルを割り振る
            labels[v] = label
            # 訪問済みにする
            visited[v] = True
            # キューに入れる
            que.append(v)



# 質問の入力と出力
q = int(input())
for _ in range(q):
    s, t = map(int, input().split())
    if labels[s] == labels[t]:
        print('yes')
    else:
        print('no')

# デバッグ用出力
# q = int(input())
# ans = []
# for _ in range(q):
#     s, t = map(int, input().split())
#     if labels[s] == labels[t]:
#         ans.append('yes')
#     else:
#         ans.append('no')
# for i in ans:
#     print(i)
