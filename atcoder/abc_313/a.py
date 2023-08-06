n = int(input())
p = list(map(int, input().split()))

if n == 1:
    print(0)
    exit(0)

m = max(p[1:])
if p[0] > m:
    print(0)
else:
    print(m - p[0] + 1)
