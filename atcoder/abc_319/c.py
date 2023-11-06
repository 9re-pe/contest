import itertools

nums = []
for _ in range(3):
    nums += list(map(int, input().split()))

orders = list(itertools.permutations(range(9)))

rows = [
    {0, 1, 2},
    {3, 4, 5},
    {6, 7, 8},
    {0, 3, 6},
    {1, 4, 7},
    {2, 5, 8},
    {0, 4, 8},
    {2, 4, 6}
]

cnt = 0
s = 0
for order in orders:
    disappoint = False
    s += 1
    for row in rows:
        li = []
        for pos in order:
            if pos in row:
                li.append(pos)
        if nums[li[0]] == nums[li[1]]:
            disappoint = True
            break
    if not disappoint:
        cnt += 1

print(cnt / s)
