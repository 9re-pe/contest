a, b = map(int, input().split())

if a == 0:
    ans = 0
else:
    ans = round(b/a, 3)
print('{:.3f}'.format(ans))
