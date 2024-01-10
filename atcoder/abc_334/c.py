from itertools import accumulate


n, k = map(int, input().split())
a = list(map(int, input().split()))
INF = 10 ** 17

# kが偶数の時
if k % 2 == 0:
    ans = 0
    for i in range(0, k, 2):
        ans += a[i+1] - a[i]
    print(ans)

# kが奇数の時
else:
    # 左から見た時の累積和
    left = []
    for i in range(k // 2):
        left.append(a[i * 2 + 1] - a[i * 2])
    s = [0] + list(accumulate(left))
    # 右から見た時の累積和
    right = []
    for i in reversed(range(k // 2)):
        right.append(a[i * 2 + 2] - a[i * 2 + 1])  # 最後に(i=0で)0が余るところを考えればわかりやすい
    t = [0] + list(accumulate(right))

    ans = INF
    # どこを余らせるか
    # 奇数番目(インデックスは偶数)だけ考えれば良い
    for i in range(k // 2 + 1):
        ans = min(ans, s[i] + t[k // 2 - i])  # 最大 - iで逆インデックス考えられる
    print(ans)
