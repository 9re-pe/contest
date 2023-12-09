n, m, l = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ng = set()
for _ in range(l):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    ng.add((c, d))

# 副菜をソート
b_sort = sorted([(b[i], i) for i in range(m)], reverse=True)

ans = -1
# 各主菜について(1変数固定)
for i, ai in enumerate(a):
    # 高い副菜からみて効率化
    for bj, j in b_sort:
        if (i, j) not in ng:
            ans = max(ans, ai + bj)
            # 主菜aiに関して以上高いことはない
            break

print(ans)
