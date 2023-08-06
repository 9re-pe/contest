n = int(input())
s = input()

ans = ''
for i in range(n):
    if s[i] == 'n' and i < n-1 and s[i+1] == 'a':
        ans += 'ny'
    else:
        ans += s[i]

print(ans)
