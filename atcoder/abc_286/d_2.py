n, x = map(int, input().split())
coins = []
for _ in range(n):
    a, b = map(int, input().split())
    coins += [a] * b

dp = [[False] * (x+1) for _ in range(len(coins)+1)]
dp[0][0] = True
for i in range(len(coins)):
    coin = coins[i]
    for j in range(x+1):
        if dp[i][j]:
            # コインを使わなかった場合
            dp[i+1][j] = True
            # コインを使った場合
            if j + coin <= x:
                dp[i+1][j+coin] = True

if dp[len(coins)][x]:
    print('Yes')
else:
    print('No')
