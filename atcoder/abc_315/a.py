b = {'a', 'i', 'u', 'e', 'o'}
s = input()
ans = ''
for c in s:
    if c not in b:
        ans += c
print(ans)
