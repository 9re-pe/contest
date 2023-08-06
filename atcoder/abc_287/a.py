n = int(input())
half = n // 2 + 1

cnt = 0
for _ in range(n):
    if input() == 'For':
        cnt += 1

if cnt >= half:
    print('Yes')
else:
    print('No')
