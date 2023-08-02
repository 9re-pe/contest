import copy

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]

for _ in range(4):
    a_cp = copy.deepcopy(a)
    # 回転
    for i in range(n):
        for j in range(n):
            a[i][j] = a_cp[n-1-j][i]
    # 判定
    ok = True
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1 and b[i][j] == 0:
                ok = False
                break
        if not ok:
            break
    if ok:
        break

if ok:
    print('Yes')
else:
    print('No')
