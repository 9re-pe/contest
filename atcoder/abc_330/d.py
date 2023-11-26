n = int(input())
grid = [list(input()) for _ in range(n)]

# 各行と各列に'o'がいくつあるか数える
rows = [0] * n
cols = [0] * n
for i in range(n):
    for j in range(n):
        if grid[i][j] == 'o':
            rows[i] += 1
            cols[j] += 1

# 条件を満たす三つ組の数を数える
count = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == 'o':
            # 同じ行または列にある他の'o'と組み合わせる
            count += (rows[i] - 1) * (cols[j] - 1)

print(count)

