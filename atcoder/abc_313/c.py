n = int(input())
a = list(map(int, input().split()))

a.sort()

total = sum(a)
small = total // n
large = small + 1
large_num = total % n

goal = [small] * (n-large_num) + [large] * large_num

cnt = 0
for i in range(n):
    cnt += abs(a[i] - goal[i])
print(cnt // 2)
