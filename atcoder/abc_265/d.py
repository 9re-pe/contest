def bs(q, left):
    global s
    global n

    left = left
    right = n

    while right - left > 1:
        mid = (left + right) // 2
        if s[mid] < q:
            left = mid
        else:
            right = mid

    if s[right] == q:
        return right
    # qが存在しなかった時
    else:
        return -1


n, p, q, r = map(int, input().split())
a = list(map(int, input().split()))

s = [0]
for i in range(n):
    s.append(s[i]+a[i])

ans = 'No'
for x in range(n+1):
    sx = s[x]

    sy = p + sx
    re = bs(sy, x)

    if re == -1:
        continue
    y = re

    sz = q + sy
    re = bs(sz, y)

    if re == -1:
        continue
    z = re

    sw = r + sz
    re = bs(sw, z)

    if re == -1:
        continue
    ans = 'Yes'
    break

print(ans)
