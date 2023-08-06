n, k = map(int, input().split())
s = list(input())

cnt = 0
ans = ''
for i in range(n):
    if s[i] == 'o' and cnt < k:
        ans += 'o'
        cnt += 1
    else:
        ans += 'x'

print(ans)
