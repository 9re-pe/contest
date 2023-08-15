"""
わかりやすかった解説
https://sugizakkworld.com/247/#toc8
"""

n = int(input())
p = list(map(int, input().split()))

pivot_i = 0
pivot_num = 0
back = []
for i in range(n-1, -1, -1):
    back.append(p[i])
    if p[i-1] > p[i]:
        pivot_i = i-1
        pivot_num = p[i-1]
        break

# back = [7, 4, 2, 1]
new_pivot_num = 0
new_back = back.copy()
for i, num in enumerate(back):
    if num < pivot_num:
        new_pivot_num = num
        new_back[i] = pivot_num
        break

ans = p[:pivot_i] + [new_pivot_num] + new_back

print(*ans)
