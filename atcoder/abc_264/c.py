h1, w1 = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h1)]
h2, w2 = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(h2)]

d = h1 + w1
ans = 'No'
for num in range(1 << d):
    rows = []
    cols = []
    for shift in range(d):
        if 1 & num >> shift == 1:
            # 行
            if shift < h1:
                rows.append(shift)
            # 列
            else:
                cols.append(shift-h1)

    # 判定
    if len(rows) != h2 or len(cols) != w2:
        continue

    ok = True
    i = 0
    for row in rows:
        j = 0
        for col in cols:
            if a[row][col] != b[i][j]:
                ok = False
            j += 1
        i += 1

    if ok:
        ans = 'Yes'
        break

print(ans)
