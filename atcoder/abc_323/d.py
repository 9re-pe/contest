import heapq
from collections import defaultdict

n = int(input())
heap = []
s2c = defaultdict(int)
for _ in range(n):
    s, c = map(int, input().split())
    heapq.heappush(heap, s)
    s2c[s] = c

ans = 0
while len(heap) != 0:
    s = heapq.heappop(heap)
    c = s2c[s]
    ans += c % 2

    if s2c[2 * s] == 0 and c // 2 != 0:
        heapq.heappush(heap, 2 * s)

    s2c[2 * s] += c // 2

print(ans)
