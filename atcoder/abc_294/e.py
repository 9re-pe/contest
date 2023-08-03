def bs(li, j):
    left = 0
    right = len(li)-1

    while right - left > 1:
        mid = (right + left) // 2

        if li[mid] < j:
            left = mid
        else:
            right = mid

    return left


L, n1, n2 = map(int, input().split())

v1 = []
l1 = []
cnt = 0
for _ in range(n1):
    v, l = map(int, input().split())
    v1.append(v)
    cnt += l
    l1.append(cnt - 1)

v2 = []
l2 = []
cnt = 0
for _ in range(n2):
    v, l = map(int, input().split())
    v2.append(v)
    cnt += l
    l2.append(cnt - 1)

ans = 0
for j in range(L):
    if v1[bs(l1, j)] == v2[bs(l2, j)]:
        ans += 1

print(ans)
