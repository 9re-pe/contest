import math


def f(n):
    global a
    global b
    return b*n + a/math.sqrt(n+1)


a, b = map(int, input().split())
x = math.pow((a**2) / (4*(b**2)), 1/3) - 1
# 誤差対策で余裕を持ってxの周り+-5個の結果を比較
left = max(int(x) - 5, 0)
right = int(x) + 5

ans = a
for n in range(left, right+1):
    ans = min(ans, f(n))

print("{:.10f}".format(ans))
