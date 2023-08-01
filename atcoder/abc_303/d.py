x, y, z = map(int, input().split())
s = input()

dp = [[0, 0] for _ in range(len(s)+1)]
for i in range(len(s)+1):
    if i == 1:
        if s[i-1] == 'A':
            dp[i][0] = y
            dp[i][1] = x + z
        else:
            dp[i][0] = x
            dp[i][1] = y + z
    else:
        if s[i-1] == 'A':
            dp[i][0] = min(dp[i-1][0] + y, dp[i-1][1] + y + z)
            dp[i][1] = min(dp[i-1][0] + x + z, dp[i-1][1] + x)
        else:
            dp[i][0] = min(dp[i-1][0] + x, dp[i-1][1] + x + z)
            dp[i][1] = min(dp[i-1][0] + y + z, dp[i-1][1] + y)

print(min(dp[len(s)]))
