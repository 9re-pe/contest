n = int(input())
xy_list = [list(map(int, input().split())) for _ in range(n)]

dp = [[0, 0] for _ in range(n+1)]

for i in range(n):
    xi = xy_list[i][0]
    yi = xy_list[i][1]
    # 料理が解毒剤入りのとき
    if xi == 0:
        # A, C, D
        dp[i + 1][0] = max(dp[i][0]+yi, dp[i][1]+yi, dp[i][0])
        # E
        dp[i + 1][1] = dp[i][1]
    # 料理が毒入りの時
    else:
        # D
        dp[i + 1][0] = dp[i][0]
        # B, E
        dp[i + 1][1] = max(dp[i][0]+yi, dp[i][1])

print(max(dp[n][0], dp[n][1]))
