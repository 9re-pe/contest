n = int(input())
s = input()

log = [(0, 0)]

x = 0
y = 0
for i in range(n):
    d = s[i]
    if d == 'R':
        x += 1
    elif d == 'L':
        x -= 1
    elif d == 'U':
        y += 1
    else:
        y -= 1
    log.append((x, y))

if len(log) == len(set(log)):
    print('No')
else:
    print('Yes')
