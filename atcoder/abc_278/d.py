from collections import defaultdict


n = int(input())
a = list(map(int, input().split()))
q = int(input())

base = 0

add = defaultdict(int)
for i in range(n):
    add[i] = a[i]


for _ in range(q):
    qe_type, *qe = map(int, input().split())

    if qe_type == 1:
        base = qe[0]
        add = defaultdict(int)

    elif qe_type == 2:
        add[qe[0]-1] += qe[1]

    else:
        print(base + add[qe[0]-1])
