from collections import deque

n, q = map(int, input().split())
que = deque()
for i in range(1, n+1):
    que.append(i)

called = deque()
gone = set()

for _ in range(q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        call = que.popleft()
        called.append(call)
    elif query[0] == 2:
        gone.add(query[1])
    else:
        roll_back = []
        while True:
            tmp = called.popleft()
            if tmp not in gone:
                print(tmp)
                # ロールバック
                called.appendleft(tmp)
                break
