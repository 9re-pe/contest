n, x = map(int, input().split())
dp = [[False] * (x+1) for _ in range(n)]

a1, b1 = map(int, input().split())
if a1 <= x:
    dp[0][a1] = True
if b1 <= x:
    dp[0][b1] = True


for i in range(1, n):
    a, b = map(int, input().split())
    for j in range(1, x+1):
        if dp[i-1][j]:
            if j + a <= x:
                dp[i][j + a] = True
            if j + b <= x:
                dp[i][j + b] = True

if dp[n-1][x]:
    print('Yes')
else:
    print('No')
