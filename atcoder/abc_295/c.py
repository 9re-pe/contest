from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
colors = set(a)

dic = defaultdict(int)
for i in range(n):
    dic[a[i]] += 1

ans = 0
for color in colors:
    ans += dic[color] // 2

print(ans)
