n = int(input())
s = input()

if '-' not in set(list(s)):
    print(-1)
    exit(0)

max_x = -1
x = 0
for i in range(n):
    if s[i] == 'o':
        x += 1
        max_x = max(max_x, x)
    else:
        x = 0

print(max_x)
