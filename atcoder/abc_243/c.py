n = int(input())
xy = []
for _ in range(n):
    x, y = map(int, input().split())
    xy.append((x, y))
s = list(input())

yxs = []
for i in range(n):
    x = xy[i][0]
    y = xy[i][1]
    si = s[i]
    # Rを優先にする
    # (同じ座標はないのでいらなかった)
    if si == 'R':
        si = '0'
    else:
        si = '1'
    yxs.append((y, x, si))
yxs.sort()

li_s = [yxs[0][2]]
for i in range(1, n):
    if yxs[i][0] == yxs[i-1][0]:
        li_s[-1] += yxs[i][2]
    else:
        li_s.append(yxs[i][2])

for s in li_s:
    if '01' in s:
        print('Yes')
        break
else:
    print('No')
