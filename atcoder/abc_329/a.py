s = input()
ans = ''
for i, c in enumerate(s):
    if i == 0:
        ans += c
    else:
        ans += " " + c
print(ans)
