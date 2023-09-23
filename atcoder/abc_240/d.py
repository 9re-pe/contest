from collections import deque


n = int(input())
a = list(map(int, input().split()))

total = 0
cnt_stk = deque()
cnt_stk.append(0)
top_stk = deque()
top_stk.append(0)
for ai in a:
    total += 1
    if ai == top_stk[-1]:
        cnt_stk[-1] += 1
        if cnt_stk[-1] == top_stk[-1]:
            total -= cnt_stk[-1]
            cnt_stk.pop()
            top_stk.pop()
    else:
        top_stk.append(ai)
        cnt_stk.append(1)
    print(total)
