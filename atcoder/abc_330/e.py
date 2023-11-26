n, q = map(int, input().split())
a = list(map(int, input().split()))

# 頻度配列の初期化
freq = [0] * (n + 2)
for ai in a:
    if ai <= n:
        freq[ai] += 1

# 現在のMEXを求める
mex = 0
for i in range(n + 2):
    if freq[i] == 0:
        mex = i
        break

for _ in range(q):
    i, x = map(int, input().split())

    # A[i]の値が変更される前に、頻度配列を更新
    if a[i - 1] <= n:
        freq[a[i - 1]] -= 1
        if freq[a[i - 1]] == 0 and a[i - 1] < mex:
            mex = a[i - 1]

    # A[i]を新しい値xに更新
    a[i - 1] = x
    if x <= n:
        freq[x] += 1
        # 新しい値が現在のMEXより小さい場合、MEXを更新する必要がある
        if x == mex:
            while freq[mex] > 0:
                mex += 1

    print(mex)
