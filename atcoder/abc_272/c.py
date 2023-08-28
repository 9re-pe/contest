n = int(input())
a = list(map(int, input().split()))

if n == 2 and a[0] % 2 != a[1] % 2:
    print(-1)
    exit(0)

a.sort()
even = []
odd = []
for ai in a:
    if ai % 2 == 0:
        even.append(ai)
    else:
        odd.append(ai)

if len(even) <= 1:
    print(odd[-1] + odd[-2])
elif len(odd) <= 1:
    print(even[-1] + even[-2])
else:
    print(max(even[-1]+even[-2], odd[-1]+odd[-2]))
