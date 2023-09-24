k = int(input())
nums = []
d = 10  # 0~9

for mask in range(1 << d):
    num = ''
    for shift in range(d):
        if 1 & mask >> shift == 1:
            num = str(shift) + num

    if num == '' or num == '0':
        continue

    nums.append(int(num))

nums.sort()
print(nums[k-1])
