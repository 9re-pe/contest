from collections import defaultdict


n = int(input())
a = list(map(int, input().split()))

a_set_sorted = sorted(list(set(a)))
dic1 = defaultdict(int)
m = len(a_set_sorted)
for i in range(m):
    dic1[a_set_sorted[i]] = m-i-1

dic2 = defaultdict(int)
for ai in a:
    dic2[dic1[ai]] += 1

for k in range(n):
    print(dic2[k])
