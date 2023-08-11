t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    cnt = 0
    for i in a:
        if i % 2 == 1:
            cnt += 1
    print(cnt)
