"""bit全探索(TLE)"""

n = int(input())
a = []
b = []
for _ in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)

cnt = 0
for num in range(1 << n):
    li = []

    for shift in range(n):
        # 裏返す
        if 1 & num >> shift == 1:
            li.append(b[shift])
        # 裏返さない
        else:
            li.append(a[shift])

    # 条件判定
    ok = True
    for i in range(n-1):
        if li[i] == li[i+1]:
            ok = False
            break

    if ok:
        cnt += 1

print(cnt % 998244353)
