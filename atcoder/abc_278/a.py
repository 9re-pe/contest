n, k = map(int, input().split())
a = list(map(int, input().split()))

if k <= n:
    ans = a[k:] + [0]*k
else:
    ans = [0] * n

print(*ans)
