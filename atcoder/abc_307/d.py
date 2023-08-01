from collections import deque
 
n = int(input())
s = list(input())

start_num = 0
stack = deque([])
for i in range(n):
    if s[i] == ')':
        if start_num >= 1:
            while True:
                if stack.pop() == '(':
                    break
            start_num -= 1
        else:
            stack.append(s[i])
    elif s[i] == '(':
        start_num += 1
        stack.append(s[i])
    else:
        stack.append(s[i])

print(''.join(map(str, stack)))
