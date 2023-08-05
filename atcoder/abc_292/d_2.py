"""
ダメなコード

指摘1
あなたのコードの問題点は、エッジの数を2倍に数えてしまっていることです。
無向グラフでは、エッジ(u, v)はエッジ(v, u)と同じです。
しかし、あなたのコードではこれらを別々のエッジとして数えてしまっています。
したがって、エッジの数を正しく数えるためには、エッジの数を2で割る必要があります。

指摘2(指摘1修正後)
あなたのコードは、各連結成分のノードとエッジを独立して数えています。
これでは、自己ループや多重辺を正しく扱うことができません。
例えば、入力例1では、ノード1は自己ループを持っています。
これは1つのエッジとして数えられますが、あなたのコードでは2つのエッジとして数えられてしまいます。
したがって、各連結成分のノードとエッジを正しく数えるためには、
各ノードとエッジを訪れるたびにそれぞれの数を1増やすのではなく、
各連結成分を訪れるたびにノードとエッジの数を数える必要があります。
-> 隣接リスト表現にすると解決できる
"""

from collections import deque, defaultdict

n, m = map(int, input().split())
graph = [[0]*n for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u][v] = 1
    graph[v][u] = 1

labels = [-1] * n
edge_nums = defaultdict(int)

visited = [False] * n

label = 0
while True:
    que = deque()

    label += 1
    edge_num = 0

    # 始点の設定
    s = -1
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

        for v in range(n):
            # エッジがない場合
            if graph[u][v] == 0 and graph[v][u] == 0:
                continue

            edge_num += 1

            if visited[v]:
                continue

            labels[v] = label
            visited[v] = True

            que.append(v)

    # エッジの数を2で割る(指摘1)
    edge_nums[label] = edge_num // 2

node_nums = defaultdict(int)
for i in range(n):
    node_nums[labels[i]] += 1

label_set = set(labels)
ans = 'Yes'
for label in label_set:
    if node_nums[label] != edge_nums[label]:
        ans = 'No'
        break

print(ans)
