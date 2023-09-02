n, q = map(int, input().split())
s = list(input())

cnt = 0
for _ in range(q):
    t, x = map(int, input().split())

    if t == 1:
        cnt = (cnt + x) % n
    else:
        print(s[(x - 1 - cnt) % n])
