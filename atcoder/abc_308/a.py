num_list = list(map(int, input().split()))
sorted_list = sorted(num_list)

ans = True

if num_list != sorted_list:
    ans = False

if sorted_list[0] < 100 or sorted_list[7] > 675:
    ans = False

for i in num_list:
    if i % 25 != 0:
        ans = False
        break

if ans:
    print('Yes')
else:
    print('No')


