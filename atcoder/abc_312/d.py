s = input()
n = len(s)
MOD = 998244353

dp = [[0 for j in range(n+2)] for i in range(n+1)]
dp[0][0] = 1
for i in range(1, n+1):
    for j in range(n+1):
        if s[i-1] == '?':
            if j == 0:
                dp[i][j] = dp[i-1][j+1]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
        elif s[i-1] == '(':
            if j != 0:
                dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j+1]

ans = dp[n][0] % MOD
print(ans)
