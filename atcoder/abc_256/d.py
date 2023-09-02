"""高校数学で習う、数直線上に黒丸と白丸で閉区間と開区間表すやつを描いて考える"""

n = int(input())
nums = set()
num2color = {}
for _ in range(n):
    l, r = map(int, input().split())
    nums.add(l)
    nums.add(r)
    num2color[l] = 'b'
    # 黒と白は黒が優先
    if r not in num2color:
        num2color[r] = 'w'

nums = list(nums)
nums.sort()

ranges = []
cur_left = nums[0]
cur_color = 'b'
for i, num in enumerate(nums):
    if i == len(nums) - 1:
        ranges.append([cur_left, num])
        break

    if cur_color == 'b':
        if num2color[num] == 'w':
            cur_color = 'w'

    else:
        if num2color[num] == 'b':
            ranges.append([cur_left, nums[i - 1]])
            cur_left = num
            cur_color = 'b'

for rng in ranges:
    print(*rng)
