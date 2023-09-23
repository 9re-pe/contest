from collections import deque


n, k = map(int, input().split())
s = input()

s2 = deque()
s2.append('X')
for c in s:
    if c == 'U':
        if s2[-1] == 'L' or s2[-1] == 'R':
            s2.pop()
        else:
            s2.append(c)
    else:
        s2.append(c)
s2.popleft()

cur = k
for c in s2:
    if c == 'U':
        cur = cur // 2
    elif c == 'L':
        cur = 2 * cur
    else:
        cur = 2 * cur + 1

print(cur)

