from collections import deque


n = int(input())
stk = deque()
for _ in range(n):
    stk.append(input())

while stk:
    s = stk.pop()
    print(s)
