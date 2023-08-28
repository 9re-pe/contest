n, m = map(int, input().split())
a = list(map(int, input().split()))

t = []
for i in range(n-m+1):
    if i == 0:
        ti = sum(a[:m])
    else:
        ti = t[i-1] - a[i-1] + a[i+m-1]
    t.append(ti)

s = []
for i in range(n-m+1):
    if i == 0:
        si = 0
        for j in range(m):
            si += (j+1) * a[j]
    else:
        si = s[i-1] - t[i-1] + m*a[i+m-1]
    s.append(si)

print(max(s))
