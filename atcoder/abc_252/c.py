from collections import defaultdict


n = int(input())
rails = []
for _ in range(n):
    rails.append(list(map(int, list(input()))))

ans = 10 ** 10
for i in range(10):
    # 絵柄iの位置を記録
    li = []
    for rail in rails:
        li.append(rail.index(i))
    # print(f'i={i} : {li}')

    # ダブりなし
    if len(li) == len(set(li)):
        ans = min(ans, max(li))
        continue

    # ダブりあり
    dic = defaultdict(int)
    for t in li:
        dic[t] += 1
    top = 0
    num_top = 0
    for key, value in dic.items():
        if value > num_top or value == num_top and key > top:
            num_top = value
            top = key
    ans = min(ans, 10 * (num_top-1) + top)

print(ans)
