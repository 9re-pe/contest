n, m, d = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

a_max = a.pop()
b_max = b.pop()
while True:
    if abs(a_max - b_max) <= d:
        print(a_max + b_max)
        break
    else:
        if a_max > b_max:
            if len(a) <= 0:
                print(-1)
                break
            a_max = a.pop()
        else:
            if len(b) <= 0:
                print(-1)
                break
            b_max = b.pop()

