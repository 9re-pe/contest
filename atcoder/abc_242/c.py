mod = 998244353
n = int(input())
dp = [[0] * 9 for _ in range(n)]
dp[0] = [1] * 9

for i in range(1, n):
    for j in range(9):
        # 1列目
        if j == 0:
            dp[i][j] = (dp[i-1][j] + dp[i-1][j+1]) % mod
        # 9列目
        elif j == 8:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % mod
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]) % mod

print(sum(dp[n-1]) % mod)
