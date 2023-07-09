a, b = map(int, input().split())

if a % 3 == 1:
    ans = (b == a + 1)
elif a % 3 == 2:
    ans = (b == a - 1 or b == a + 1)
else:
    ans = (b == a - 1)

if ans:
    print('Yes')
else:
    print('No')
