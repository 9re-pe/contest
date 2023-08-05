import itertools

h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

when_r_list = list(itertools.combinations(range((h-1) + (w-1)), (w-1)))
routes = []
for when_r in when_r_list:
    route = []
    when_r = set(when_r)
    for i in range((h-1) + (w-1)):
        if i in when_r:
            route.append('r')
        else:
            route.append('d')
    routes.append(route)

ans = 0
for route in routes:
    i = 0
    j = 0
    nums = {a[i][j]}
    for direction in route:
        if direction == 'r':
            j += 1
            nums.add(a[i][j])
        else:
            i += 1
            nums.add(a[i][j])
    if len(nums) == len(route) + 1:
        ans += 1

print(ans)
