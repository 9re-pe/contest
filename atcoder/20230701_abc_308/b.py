n, m = map(int, input().split())
eat = list(input().split())  # C

d = ['other']
d = d + list(input().split())
d_set = set(d[1:])
p = list(map(int, input().split()))

color_to_price = {}
for i in range(m+1):
    color_to_price[d[i]] = p[i]

ans = 0
for c in eat:
    if c in d_set:
        ans += color_to_price[c]
    else:
        ans += color_to_price['other']

print(ans)
