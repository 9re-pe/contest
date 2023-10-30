import bisect


n, m, p = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()

s = [0]
for i, bi in enumerate(b):
    s.append(bi + s[-1])

ans = 0
for ai in a:
    k = bisect.bisect_right(b, p - ai)
    ans += p * (m - k)
    ans += ai * k
    ans += s[k]

print(ans)
