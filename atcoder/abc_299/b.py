n, t = map(int, input().split())
c = list(map(int, input().split()))
r = list(map(int, input().split()))

win = 0
if t in set(c):
    color = t
else:
    color = c[0]

max_r = 0
ans = -1
for i in range(n):
    if c[i] == color and r[i] > max_r:
        ans = i
        max_r = r[i]

print(ans+1)
