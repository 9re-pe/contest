n, q = map(int, input().split())
status = [0] * (n+1)

for _ in range(q):
    c, x = map(int, input().split())
    if c == 1:
        status[x] += 1
    elif c == 2:
        status[x] += 2
    else:
        if status[x] >= 2:
            print('Yes')
        else:
            print('No')
