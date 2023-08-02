import heapq
from collections import defaultdict

n = int(input())
q = int(input())

# key:box_num
box = defaultdict(list)
# key:card_num
card = defaultdict(set)

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        i, j = query[1], query[2]
        heapq.heappush(box[j], i)
        card[i].add(j)
    elif query[0] == 2:
        i = query[1]
        sorted_box = box[i].copy()  # リストのコピーを作成
        while sorted_box:  # リストが空になるまでループ
            print(heapq.heappop(sorted_box), end=' ')  # 最小値を取り出して出力
        print()  # 改行
    else:
        i = query[1]
        print(*sorted(card[i]))
