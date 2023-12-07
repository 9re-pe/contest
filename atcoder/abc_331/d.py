# WA

n, q = map(int, input().split())
p = [input() for _ in range(n)]

# Pのパターンから各セルが黒マスかどうかを表すNxNの二次元配列blackを作成します。
# P[i][j]が'B'ならblack[i][j]は1、そうでなければ0です。
black = [[1 if p[i % n][j % n] == 'B' else 0 for j in range(n)] for i in range(n)]

# black配列の累積和を計算します。
for i in range(n):
    for j in range(n):
        if i > 0:
            black[i][j] += black[i - 1][j]
        if j > 0:
            black[i][j] += black[i][j - 1]
        if i > 0 and j > 0:
            black[i][j] -= black[i - 1][j - 1]

for _ in range(q):
    a, b, c, d = map(int, input().split())
    a, b, c, d = a - 1, b - 1, c - 1, d - 1

    # クエリの長方形内の行数と列数を計算します
    rows = c - a + 1
    cols = d - b + 1

    # クエリの長方形内の完全なパターンの数を計算します
    full_patterns_row = rows // n
    full_patterns_col = cols // n

    # 完全なパターン後の余りの行数と列数を計算します
    rem_rows = rows % n
    rem_cols = cols % n

    # 完全なパターン内の黒セルの数を計算します
    full_patterns_black = full_patterns_row * full_patterns_col * black[n - 1][n - 1]

    # 余りの行と列の黒セルの数を計算します
    rem_row_black = full_patterns_col * (black[rem_rows - 1][n - 1] if rem_rows > 0 else 0)
    rem_col_black = full_patterns_row * (black[n - 1][rem_cols - 1] if rem_cols > 0 else 0)

    # 余りの行と列の交差部分の黒セルの数を計算します
    intersection_black = black[rem_rows - 1][rem_cols - 1] if rem_rows > 0 and rem_cols > 0 else 0

    # 全ての黒セルの数を合計します
    print(full_patterns_black + rem_row_black + rem_col_black + intersection_black)
