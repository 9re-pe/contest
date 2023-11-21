from collections import defaultdict


n = int(input())
s = input()
d = defaultdict(int)
d[s[0]] = 1

cnt = 1
for i in range(1, n):
    if s[i] == s[i-1]:
        cnt += 1
    else:
        d[s[i-1]] = max(d[s[i-1]], cnt)
        cnt = 1
d[s[n-1]] = max(d[s[n-1]], cnt)

ans = 0
for c in "abcdefghijklmnopqrstuvwxyz":
    ans += d[c]
print(ans)
