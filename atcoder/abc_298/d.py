from collections import deque

mod = 998244353
q = int(input())
num = 1
que = deque([1])

# 10の冪乗を先に計算する
pow10 = [1] * (q + 1)
for i in range(1, q + 1):
    pow10[i] = (10 * pow10[i - 1]) % mod

for _ in range(q):
    qe = list(map(int, input().split()))

    if qe[0] == 1:
        num = (10 * num + qe[1]) % mod
        que.append(qe[1])

    elif qe[0] == 2:
        top = que.popleft()
        d = len(que)
        num = (num - top * pow10[d]) % mod

    else:
        print(num)
