n, d = map(int, input().split())
matrix = [[0 for j in range(d)] for i in range(n)]
for i in range(n):
    s = list(input())
    for j in range(d):
        if s[j] == 'o':
            matrix[i][j] = 1

day = 0
max_day = 0
for j in range(d):
    ok_day = True
    for i in range(n):
        if matrix[i][j] == 0:
            ok_day = False
    if ok_day:
        day += 1
        max_day = max(max_day, day)
    else:
        day = 0

print(max_day)
