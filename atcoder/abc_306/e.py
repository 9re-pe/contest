n, k, q = map(int, input().split())
xy_list = [list(map(int, input().split())) for _ in range(q)]

a = [0] * n
bk = 0
f = 0

for xy in xy_list:
    x = xy[0]
    y = xy[1]

    if y < bk:
        print(f)
    else:
        # bkの更新
        f += y
        f -= a[x-1]
        a[x-1] = y
        print(f)

