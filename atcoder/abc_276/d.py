n = int(input())
a = list(map(int, input().split()))

xyz = []
x_li = []
y_li = []
z_set = set()
for i in range(n):

    x = 0
    while a[i] % 2 == 0:
        x += 1
        a[i] //= 2

    y = 0
    while a[i] % 3 == 0:
        y += 1
        a[i] //= 3

    z = a[i]

    x_li.append(x)
    y_li.append(y)
    z_set.add(z)

if len(z_set) != 1:
    print(-1)
    exit(0)

x_min = min(x_li)
y_min = min(y_li)
cnt = 0
for i in range(n):
    cnt += (x_li[i] - x_min) + (y_li[i] - y_min)

print(cnt)
