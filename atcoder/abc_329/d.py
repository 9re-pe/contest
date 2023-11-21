from collections import defaultdict


n, m = map(int, input().split())
a = list(map(int, input().split()))
d = defaultdict(int)

pre = 0
for i in range(m):
    d[a[i]] += 1

    if i == 0:
        pre = a[i]
        print(pre)
    elif pre == a[i]:
        print(pre)
    else:
        # 開票された人が勝った場合
        if d[a[i]] > d[pre] or (d[a[i]] == d[pre] and a[i] < pre):
            pre = a[i]
            print(pre)
        # preが勝った場合
        else:
            print(pre)
