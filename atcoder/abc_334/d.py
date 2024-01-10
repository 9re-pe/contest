n, q = map(int, input().split())
r = list(map(int, input().split()))
r.sort()
s = [0]
for i in range(n):
    s.append(s[-1] + r[i])
INF = 10 ** 15
s.append(INF)

for i in range(q):
    x = int(input())

    l = 0
    r = n + 1

    while r - l > 1:
        m = (l + r) // 2
        if s[m] <= x:
            l = m
        else:
            r = m

    print(l)
