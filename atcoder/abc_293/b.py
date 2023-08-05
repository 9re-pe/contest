n = int(input())
a = list(map(int, input().split()))

called = [False] * n
for i in range(n):
    if called[i]:
        continue
    called[a[i]-1] = True

cnt = 0
ans = []
for i in range(n):
    if not called[i]:
        cnt += 1
        ans.append(i+1)

print(cnt)
print(*ans)
