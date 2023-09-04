n, d, p = map(int, input().split())
f = list(map(int, input().split()))
f.sort(reverse=True)

x_max = (n + d - 1) // d  # 切り上げ
f_sum = sum(f)
x = 0
ans = f_sum
for i in range(n):
    f_sum -= f[i]

    if (i+1) % d == 0:
        x += 1
        ans = min(ans, f_sum+p*x)

ans = min(ans, p*(x+1))

print(ans)
