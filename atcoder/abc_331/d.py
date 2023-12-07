def f(x, y):
    """左上(0, 0), 右下(x, y)の長方形中の黒マスの個数を求める"""
    re  = s[x % n][y % n]                # 右下
    re += s[n][n] * (x // n) * (y // n)  # 左上
    re += s[n][y % n] * (x // n)         # 右上
    re += s[x % n][n] * (y // n)         # 左下

    return re


n, q = map(int, input().split())
p = [list(input()) for _ in range(n)]

# 番兵を入れる
s = [[0] * (n+1) for _ in range(n+1)]

# 文字を01に変換
for i in range(n):
    for j in range(n):
        s[i+1][j+1] = int(p[i][j] == 'B')
# 二次元累積和に変換
# 行方向
for i in range(n):
    for j in range(n):
        s[i+1][j+1] += s[i+1][j]
# 列方向
for i in range(n):
    for j in range(n):
        s[i+1][j+1] += s[i][j+1]

for _ in range(q):
    a, b, c, d = map(int, input().split())
    c += 1
    d += 1
    ans = f(c, d) - f(a, d) - f(c, b) + f(a, b)
    print(ans)
