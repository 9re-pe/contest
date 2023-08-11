from collections import deque

s = input()
n = len(s)

box = set()
stack = deque()
ans = 'Yes'
for i in range(n):
    if s[i] == '(':
        stack.append(s[i])
    elif s[i] == ')':
        while True:
            c = stack.pop()
            if c == '(':
                break
            else:
                box.remove(c)
    else:
        if s[i] in box:
            ans = 'No'
            break
        stack.append(s[i])
        box.add(s[i])

print(ans)
