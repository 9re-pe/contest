import sys
sys.setrecursionlimit(10**9)


def dfs(i):
    global n
    global x
    global a
    global b
    global ans
    global total

    if total == x:
        ans = 'Yes'

    if total > x or i >= n:
        return

    for num in range(b[i]+1):
        tmp = total
        total += a[i] * num
        dfs(i+1)
        # ロールバック
        total = tmp


n, x = map(int, input().split())
a = []
b = []
for _ in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)
ans = 'No'
total = 0

dfs(0)

print(ans)
