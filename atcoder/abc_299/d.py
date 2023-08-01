n = int(input())
left = 1
right = n

while right - left > 1:
    center = (left + right) // 2
    print(f"? {center}")
    s = int(input())
    if s == 1:
        right = center
    else:
        left = center

print(f"! {left}")
