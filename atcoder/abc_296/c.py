n, x = map(int, input().split())
a = list(map(int, input().split()))

ai = set(a)
aj_plus_x = {i + x for i in ai}

if len(ai & aj_plus_x) == 0:
    print('No')
else:
    print('Yes')
