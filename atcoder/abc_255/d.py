def ans(x, k):
    """
    Σ_{i=1}^{k}(X - a_i) + Σ_{i=k+1}^{n}(a_i - X)
    を変形
    """
    if k == n+1:
        return n*x - s[n]

    return s[n] - 2*s[k] - n*x + 2*k*x


n, q = map(int, input().split())
a = [-1] + list(map(int, input().split()))
a.sort()

s = [0]
for i, ai in enumerate(a):
    if i == 0:
        continue
    s.append(s[-1] + ai)

for _ in range(q):
    x = int(input())

    if x > a[-1]:
        k = n+1
    elif x < a[1]:
        k = 0
    else:
        # 二分探索
        left = 1
        right = n

        while right - left > 1:
            mid = (left + right) // 2

            if x > a[mid]:
                left = mid
            else:
                right = mid

        k = left
    print(ans(x, k))
