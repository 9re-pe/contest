"""DP"""

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = set(map(int, input().split()))
x = int(input())

dp = [False] * (x + 1 + max(a))
dp[0] = True

for i in range(x + 1):
    if dp[i]:
        for step in a:
            if i + step not in b:
                dp[i + step] = True

if dp[x]:
    print('Yes')
else:
    print('No')
