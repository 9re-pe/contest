from collections import defaultdict


n = int(input())
a = list(map(int, input().split()))

start = 0
dic = defaultdict(int)
for i in range(n):
    ai = a[i]
    if ai == -1:
        start = i+1
    else:
        dic[ai] = i+1

ans = [start]
ref = start
for i in range(n-1):
    nxt = dic[ref]
    ans.append(nxt)
    ref = nxt

print(*ans)
