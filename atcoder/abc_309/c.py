n, k = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]

# 最大で飲む量(bの和をとる)
total = 0
for row in ab:
    total += row[1]

# a(日)の値でソートする
sorted_ab = sorted(ab)

ans = 0
if total <= k:
    ans = 1
else:
    for row in sorted_ab:
        total -= row[1]
        if total <= k:
            ans = row[0] + 1
            break

print(ans)
