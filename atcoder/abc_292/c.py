"""
N = 7のとき

AB | 1 2 3 4 5 6
-----------------
CD | 6 5 4 3 2 1

例えば、AB = 6を満たすABは
    (1,6), (2,3), (3,2), (6,1)
でこれは約数の個数に等しい

上下の約数の個数をかけたものを合計すれば良い
"""

n = int(input())
# divisors[4] = 4の約数の個数
divisors = [0] * (n+1)

# 約数の数を計算する
for i in range(1, n+1):
    for j in range(i, n+1, i):
        divisors[j] += 1

ans = 0
for i in range(1, n):
    ans += divisors[i] * divisors[n-i]

print(ans)

