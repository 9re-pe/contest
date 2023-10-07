n, m = map(int, input().split())
a = list(map(int, input().split()))

ans = []
j = 0  # aのインデックス
for i in range(n):
    day = i + 1
    ans.append(a[j] - day)
    if day == a[j]:
        j += 1

for x in ans:
    print(x)
