a = list(map(int, input().split()))

ans = 0
for i, ai in enumerate(a):
    if ai == 1:
        ans += 2 ** i

print(ans)
