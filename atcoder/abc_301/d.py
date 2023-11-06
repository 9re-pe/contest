s = input()
d = len(s)
t = s.replace('?', '0')
n = bin(int(input()))[2:].rjust(d, '0')

if int(t, 2) > int(n, 2):
    print(-1)
    exit(0)

ans = ''
for i in range(d):
    if s[i] == '?':
        if i == d - 1:
            if int(ans + '1', 2) <= int(n, 2):
                ans += '1'
            else:
                ans += '0'
        else:
            if int(ans + '1' + t[i+1:], 2) <= int(n, 2):
                ans += '1'
            else:
                ans += '0'
    else:
        ans += s[i]

print(int(ans, 2))
