"""
考え方

1. 横と縦別々で考える（同じことをやればいい）
2. 1行(列)ずつみていく（行(列)で独立性がある）

-> この時点で1次元問題に帰着する
-> 行(列)の数よりO(H)(O(W))なので，1行(列)の処理をO(W)(O(H))でできれば良い

3. 幅Kの中に
    - xがなければOK
    - .の数が操作数

4. 1マスずつみていってKを先までみていけば良い？
-> O(WK)となり，Kは大きいので無視できない
-> 累積和 or 差分計算
-> 実装が簡単な差分計算でやる

5. xと.の数をそれぞれ保持しておく
    - xが0になったらansを.の数でmin更新
"""
h, w, k = map(int, input().split())
grid = [list(input()) for _ in range(h)]
INF = 10 ** 10
ans = INF


def solve(x, y):
    global ans

    if y < k:
        return

    for i in range(x):
        xn = grid[i][:k].count("x")
        dn = grid[i][:k].count(".")
        for j in range(y - k + 1):
            if xn == 0:
                ans = min(ans, dn)
            if j + k < y:
                xn -= int(grid[i][j] == "x")
                xn += int(grid[i][j + k] == "x")
                dn -= int(grid[i][j] == ".")
                dn += int(grid[i][j + k] == ".")


# 横方向
solve(h, w)

# 転置
grid = [list(x) for x in zip(*grid)]

# 縦方向
solve(w, h)

if ans == INF:
    print(-1)
else:
    print(ans)
