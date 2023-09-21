n, m, k = map(int, input().split())
mod = 998244353
dp = [[0] * (k+1) for _ in range(n+1)]
dp[0][0] = 1

for i in range(n):
    for j in range(k):
        for t in range(1, m+1):
            if j + t > k:
                break
            dp[i+1][j+t] += dp[i][j]
            dp[i+1][j+t] %= mod

print(sum(dp[-1]) % mod)
