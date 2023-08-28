n, x, y = map(int, input().split())

r = [0] * (n-1) + [1]
b = [0] * n

# 赤がレベル1だけになるまで
while sum(r[1:]) > 0:
    # 赤の変換
    for lv in range(n-1, 0, -1):  # 大きい順
        num = r[lv]
        r[lv] = 0
        r[lv-1] += num
        b[lv] += x * num

    # 青の変換
    for lv in range(n - 1, 0, -1):  # 大きい順
        num = b[lv]
        b[lv] = 0
        r[lv-1] += num
        b[lv-1] += y * num

print(b[0])
