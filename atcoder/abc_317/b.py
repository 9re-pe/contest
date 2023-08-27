n = int(input())
a = list(map(int, input().split()))
a.sort()
for i in range(n-1):
    if a[i+1] - a[i] != 1:
        print(a[i]+1)
        break
