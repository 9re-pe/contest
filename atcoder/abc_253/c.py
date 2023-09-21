from collections import defaultdict
import heapq


q = int(input())
s = defaultdict(int)
min_heap = []
max_heap = []

for _ in range(q):
    qe = list(map(int, input().split()))
    t = qe[0]

    if t == 1:
        x = qe[1]
        s[x] += 1
        heapq.heappush(min_heap, x)
        heapq.heappush(max_heap, -x)

    elif t == 2:
        x = qe[1]
        c = qe[2]
        s[x] -= min(c, s[x])

    else:
        while True:
            p = heapq.heappop(min_heap)

            if s[p] > 0:
                mn = p
                # ロールバック
                heapq.heappush(min_heap, p)
                break

        while True:
            p = heapq.heappop(max_heap)

            if s[-p] > 0:
                mx = -p
                # ロールバック
                heapq.heappush(max_heap, p)
                break

        print(mx - mn)
