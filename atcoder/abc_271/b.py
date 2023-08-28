n, q = map(int, input().split())
arr = []
for _ in range(n):
    l, *a = map(int, input().split())
    arr.append(a)
for _ in range(q):
    s, t = map(int, input().split())
    print(arr[s-1][t-1])
