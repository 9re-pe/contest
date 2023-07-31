import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix

# 2点間の距離dを計算
def get_d(a, b):
    npa = np.array(a)
    npb = np.array(b)
    d = np.linalg.norm(npb - npa)

    return d

# 入力
n, D = map(int, input().split())
people_list = []
for i in range(n):
    people_list.append(list(map(int, input().split())))

# グラフの生成(隣接行列)
graph = []
for i in range(n):
    row = []
    for j in range(n):
        if i == j:
            row.append(0)
            continue
        # 自分
        a = people_list[i]
        # 相手
        b = people_list[j]

        d = get_d(a, b)
        # 距離d以内ならエッジを追加
        if d <= D:
            row.append(1)
        else:
            row.append(0)
    graph.append(row)

#print(graph)

# 連結成分の抽出
# np_graph = np.array(graph)
np_graph = csr_matrix(graph)
_, labels = connected_components(np_graph)

# 人1のラベルを抽出
label_0 = labels[0]
# 人1と同じ連結成分に属する人をYesとして出力
for i in range(n):
    if labels[i] == label_0:
        print('Yes')
    else:
        print('No')