n, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

mn = a[0]
mx = a[-1]
total = sum(a[1:-1])

sub = x - total
if sub > mx:
    print(-1)
    exit(0)

if sub <= mn:
    print(0)
    exit(0)

print(sub)
