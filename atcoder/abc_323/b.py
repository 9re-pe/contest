n = int(input())
cnt_i = []
for i in range(n):
    s = input()
    cnt = s.count('o')
    cnt_i.append([cnt, -i])
cnt_i.sort(reverse=True)

ans = []
for li in cnt_i:
    ans.append(-li[1]+1)

print(*ans)
