n, t = map(int, input().split())
a = list(map(int, input().split()))

to_a = [0]
for i in range(n):
    to_a.append(to_a[-1]+a[i])

cycle = to_a[-1]
r = t % cycle

left = 0
right = n
while right - left > 1:
    mid = (right + left) // 2
    if to_a[mid] < r:
        left = mid
    else:
        right = mid

print(left+1, r-to_a[left])
