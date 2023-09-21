from collections import defaultdict
from bisect import bisect_left, bisect_right


n = int(input())
a = list(map(int, input().split()))
dic = defaultdict(list)
for i in range(n):
    dic[a[i]].append(i+1)

q = int(input())
for _ in range(q):
    l, r, x = map(int, input().split())
    li = dic[x]
    print(bisect_right(li, r) - bisect_left(li, l))
