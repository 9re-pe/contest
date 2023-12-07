n = int(input())
a = list(map(int, input().split()))

# インデックスを保持しつつソート
b = sorted([(a[i], i) for i in range(n)])

# 累積和
s = [0] * (n + 1)
for i in range(n):
    s[i + 1] = s[i] + b[i][0]

ans = []
for i in range(n):
    ai = a[i]
    # 二分探索でaiの次に大きい要素ajを見つける
    left, right = 0, n
    while left < right:
        mid = (left + right) // 2
        if b[mid][0] <= ai:
            left = mid + 1
        else:
            right = mid
    # 累積和でaj以上の要素の和をO(1)で計算
    ans.append(s[-1] - s[left])

print(*ans)
