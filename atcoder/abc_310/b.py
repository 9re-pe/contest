n, m = map(int, input().split())
items = []
for _ in range(n):
    p, c, *f = map(int, input().split())
    f = set(f)
    items.append([p, c, f])

ans = 0
for i in range(n):
    for j in range(n):
        # 条件1
        if items[i][0] >= items[j][0]:
            # 条件2
            if items[j][2].issuperset(items[i][2]):
                # 条件3
                if items[i][0] > items[j][0]:
                    ans += 1
                elif len(items[j][2]) > len(items[i][2]):
                    ans += 1

if ans > 0:
    print('Yes')
else:
    print('No')
