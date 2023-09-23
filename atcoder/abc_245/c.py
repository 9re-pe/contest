n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 1個前でA, Bの要素を使うことができるか？
a_ok = True
b_ok = True

for i in range(n-1):
    # a0, b0: 1個前の要素
    a0, a1 = a[i], a[i+1]
    b0, b1 = b[i], b[i+1]

    # 今A, Bの要素を使うことができるか
    na_ok = False
    nb_ok = False
    if a_ok:
        na_ok |= abs(a0 - a1) <= k
        nb_ok |= abs(a0 - b1) <= k
    if b_ok:
        na_ok |= abs(b0 - a1) <= k
        nb_ok |= abs(b0 - b1) <= k
    a_ok = na_ok
    b_ok = nb_ok

if a_ok or b_ok:
    print('Yes')
else:
    print('No')

