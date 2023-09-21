from collections import defaultdict


n, k = map(int, input().split())
s = []
for _ in range(n):
    s.append(list(input()))

ans = 0
for mask in range(1 << n):
    c2num = defaultdict(int)
    cnt = 0

    for shift in range(n):
        if 1 & mask >> shift == 1:
            si = s[shift]
            for c in si:
                c2num[c] += 1

    for num in c2num.values():
        if num == k:
            cnt += 1

    ans = max(ans, cnt)

print(ans)
