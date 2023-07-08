n = int(input())
ai = num_list = list(map(int, input().split()))

ans = []
week_sum = 0
for i, a in enumerate(ai):
    week_sum += a
    if i % 7 == 6:
        ans.append(week_sum)
        week_sum = 0

print(*ans)


