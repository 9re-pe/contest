n = int(input())
a = list(map(int, input().split()))
q = int(input())
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        k = query[1] - 1
        a[k] = query[2]
    else:
        k = query[1] - 1
        print(a[k])
