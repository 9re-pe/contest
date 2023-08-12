from collections import deque


n = int(input())
s = list(input())
q = int(input())

convert = 'none'
last_convert = 0
change = deque()
for i in range(q):
    t, x, c = input().split()
    t = int(t)
    x = int(x)

    if t == 2:
        convert = 'lower'
        last_convert = i
    elif t == 3:
        convert = 'upper'
        last_convert = i
    else:
        change.append([i, x-1, c])

if convert == 'none':
    while len(change) > 0:
        i, x, c = change.popleft()
        s[x] = c
else:
    cnt = 0
    not_converted = True
    while len(change) > 0:
        i, x, c = change.popleft()

        if not_converted and i > last_convert:
            not_converted = False
            s = ''.join(s)
            if convert == 'lower':
                s = s.lower()
            else:
                s = s.upper()
            s = list(s)

        s[x] = c

print(''.join(s))
