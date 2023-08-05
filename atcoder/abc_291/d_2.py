"""DP"""

n = int(input())
mod = 998244353
a = []
b = []
for _ in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)

dp = [[0, 0] for _ in range(n)]
dp[0] = [1, 1]
for i in range(1, n):
    if a[i-1] != a[i]:
        tmp1 = dp[i-1][0]
    else:
        tmp1 = 0
    if b[i-1] != a[i]:
        tmp2 = dp[i-1][1]
    else:
        tmp2 = 0

    dp[i][0] = (tmp1 + tmp2) % mod

    if a[i-1] != b[i]:
        tmp1 = dp[i-1][0]
    else:
        tmp1 = 0
    if b[i-1] != b[i]:
        tmp2 = dp[i-1][1]
    else:
        tmp2 = 0

    dp[i][1] = (tmp1 + tmp2) % mod

print(sum(dp[n-1]) % mod)
