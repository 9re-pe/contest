"""正方形は2点決まれば4点わかる"""


grid = [list(input()) for _ in range(9)]

cnt = 0
for ai in range(9):
    for aj in range(9):
        for bi in range(ai, 9):  # 辺ABを上辺にするための制約
            for bj in range(aj+1, 9):  # 辺ABを上辺にするための制約
                # A, Bが決まったとき、C, Dが条件を満たすか確かめにいく
                if grid[ai][aj] == '#' and grid[bi][bj] == '#':
                    ci = bi + (bj - aj)
                    cj = bj - (bi - ai)
                    di = ci - (bj - cj)
                    dj = cj - (ci - bi)

                    if 0 <= ci <= 8 and 0 <= di <= 8 and 0 <= cj <= 8 and 0 <= dj <= 8:
                        if grid[ci][cj] == '#' and grid[di][dj] == '#':
                            cnt += 1

print(cnt)
