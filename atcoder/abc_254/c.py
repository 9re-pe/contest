n, k = map(int, input().split())
a = list(map(int, input().split()))

# k個のグループに分ける
# このグループ内ではソートが可能
b = [[] for _ in range(k)]
for i in range(n):
    b[i % k].append(a[i])

# 各グループソートする
for i in range(k):
    b[i].sort()

sorted_a = sorted(a)
merged_b = [0] * n
for i in range(n):
    merged_b[i] = b[i % k][i // k]

if merged_b == sorted_a:
    print('Yes')
else:
    print('No')
