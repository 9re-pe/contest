n, m = map(int, input().split())

INF = 10 ** 13
ans = INF
for a in range(1, n+1):
    b = (m + a - 1) // a
    if b <= n:
        ans = min(ans, a * b)

    if a ** 2 > m:
        break

if ans == INF:
    print(-1)
else:
    print(ans)
