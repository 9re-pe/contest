n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

left = 0
right = 10**9 + 1

while right - left > 1:
    mid = (left + right) // 2
    # 条件を満たす売り手と買い手をカウント
    sale = sum(ai <= mid for ai in a)
    buy = sum(bi >= mid for bi in b)
    if sale >= buy:
        right = mid
    else:
        left = mid

print(right)
