from collections import deque

n, m = map(int, input().split())
a = set((map(int, input().split())))

stack = deque()
for i in range(1, n+1):
    if i in a:
        stack.append(i)
    else:
        print(i, end=' ')
        while len(stack) > 0:
            print(stack.pop(), end=' ')

print()
