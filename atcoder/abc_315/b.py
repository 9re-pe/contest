m = int(input())
d = list(map(int, input().split()))

mid = (sum(d)+1) // 2
month = 0
days = 0
for i in range(m):
    days += d[i]
    if mid <= days:
        month = i+1
        break
day = d[month-1] - (days - mid)

print(month, day)
