h, w = map(int, input().split())
table = [list(input()) for _ in range(h)]

ans = []
for i in range(h):
    for j in range(w):
        if table[i][j] == '.':
            cnt = 0
            # print(i, j)
            if i - 1 >= 0 and table[i - 1][j] == '#':
                cnt += 1
            if i + 1 < h and table[i + 1][j] == '#':
                cnt += 1
            if j - 1 >= 0 and table[i][j - 1] == '#':
                cnt += 1
            if j + 1 < w and table[i][j + 1] == '#':
                cnt += 1
            if cnt >= 2:
                ans = [i, j]

print('{} {}'.format(ans[0] + 1, ans[1] + 1))
