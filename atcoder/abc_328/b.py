n = int(input())
d = list(map(int, input().split()))
cnt = 0
for i in range(n):
    for j in range(d[i]):
        month = i + 1
        day = j + 1
        s = set(list(str(month))) | set(list(str(day)))
        if len(s) == 1:
            cnt += 1
print(cnt)
