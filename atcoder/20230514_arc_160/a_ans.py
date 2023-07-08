# f(L, R)
def f (a, l, r):
    reverse_range_list = list(reversed(a[l-1:r]))
    re = a[:l-1] + reverse_range_list + a[r:]

    return re

# Kの位置を返す
# 0 : 前
# 1 : 真ん中
# 2 : 後ろ
# ex : 
#   A = (3, 1, 2, 4, 5)
#   ai = 3, i = 1
def get_k_position (k, n, ai, i):
    # 現在考えている部分の要素数
    tmp_n = n - i + 1

    # 前
    if k < ai:
        return 0
    # 真ん中
    # k < 15 - 2 = 13
    # 後ろにながれるのはk = 14, 15なのでok
    elif k < tmp_n * (tmp_n + 1) / 2 - (n - ai):
        return 1
    # 後ろ
    else:
        return 0

# 入力
n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = []
for i in range(1, n+1):
    # 先頭の要素を取得
    ai = a[i - 1]
    k_position = get_k_position(k, n, ai, i)
    print(k_position)
    if k_position == 0:
        r = k - ai ??
        ans += f(a, i, r)
        break
    elif k_position == 2:
        r = 
        ans += f(a, i, r)
        break
    else:
        ans.append(ai)

# 出力
print(*ans)
