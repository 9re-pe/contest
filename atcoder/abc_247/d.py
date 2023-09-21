from collections import deque


q = int(input())
que = deque()
for _ in range(q):
    qe = list(map(int, input().split()))

    if qe[0] == 1:
        x = qe[1]
        c = qe[2]
        que.append((x, c))
    else:
        c = qe[1]
        ans = 0
        while c > 0:
            x, l = que.popleft()

            if l <= c:
                ans += x * l
                c -= l
            else:
                ans += x * c
                que.appendleft((x, l-c))
                c = 0
        print(ans)
