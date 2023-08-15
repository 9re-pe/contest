s = input()
ans = -1
for i, c in enumerate(s):
    if c == 'a':
        ans = i + 1

print(ans)
