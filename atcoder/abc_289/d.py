"""DFS(TLE)"""

import sys
sys.setrecursionlimit(10**8)


def dfs(now):
    global a
    global b
    global x
    global ans

    if now > x or now in b:
        return

    if now == x:
        ans = 'Yes'

    for i in a:
        dfs(now+i)


n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = set(map(int, input().split()))
x = int(input())
ans = 'No'

dfs(0)
print(ans)
