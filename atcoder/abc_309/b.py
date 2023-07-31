n = int(input())
a_str = [input() for _ in range(n)]
a = [[0] * n for _ in range(n)]
for i, row in enumerate(a_str):
    for j in range(n):
        a[i][j] = int(row[j])

b = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        # 外側
        if i == 0:
            if j == 0:
                b[i][j] = a[i+1][j]
            else:
                b[i][j] = a[i][j-1]
        elif i == n-1:
            if j == n-1:
                b[i][j] = a[i-1][j]
            else:
                b[i][j] = a[i][j+1]
        elif j == 0:
            if i == n-1:
                b[i][j] = a[i][j+1]
            else:
                b[i][j] = a[i+1][j]
        elif j == n-1:
            if i == 0:
                b[i][j] = a[i][j-1]
            else:
                b[i][j] = a[i-1][j]
        # 内側のマス
        else:
            b[i][j] = a[i][j]

for row in b:
    print(''.join(map(str, row)))
