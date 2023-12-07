n = int(input())
a = list(map(int, input().split()))

b = sorted([(val, idx) for idx, val in enumerate(a)])

# ステップ2: ソートされた配列の累積和を計算
s = [0] * (n + 1)
for i in range(n):
    s[i + 1] = s[i] + b[i][0]

# ステップ3 & 4: 各要素に対して、ソートされた配列での位置を二分探索で見つけ、
# その要素より大きい数の和を計算
ans = [0] * n
for val, original_idx in b:
    left, right = 0, n
    while left < right:
        mid = (left + right) // 2
        if b[mid][0] <= val:
            left = mid + 1
        else:
            right = mid
    # 現在の要素より大きい数の和を計算
    ans[original_idx] = s[-1] - s[left]

print(*ans)
