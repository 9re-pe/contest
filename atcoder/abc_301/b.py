n = int(input())
a = list(map(int, input().split()))
ans = []

for i in range(n):
    ans.append(a[i])
    if i != n-1 and abs(a[i] - a[i+1]) != 1:
        if a[i] < a[i+1]:
            for num in range(a[i]+1, a[i+1]):
                ans.append(num)
        else:
            for num in range(a[i]-1, a[i+1], -1):
                ans.append(num)

print(*ans)
