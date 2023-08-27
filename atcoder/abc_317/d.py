n = int(input())
z_li = [-1]
# 高橋くんがその選挙区を取るのに必要な鞍替え人数
p = [-1]
# 高橋くんの議席数
x_sum = 0
for _ in range(n):
    x, y, z = map(int, input().split())

    z_li.append(z)

    # 青木くんが勝つ選挙区
    if x < y:
        p.append((y-x) // 2 + 1)
    else:
        p.append(0)
        x_sum += z

# 過半数
z_sum = sum(z_li[1:])
half = z_sum // 2 + 1

if x_sum >= half:
    print(0)
    exit(0)

INF = 100000000000
dp = [[INF] * (z_sum+1) for _ in range(n+1)]
dp[0][0] = 0

for i in range(1, n+1):
    for j in range(z_sum+1):
        pi = p[i]
        zi = z_li[i]

        if j-zi < 0:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-zi]+pi)

print(min(dp[n][half:]))
