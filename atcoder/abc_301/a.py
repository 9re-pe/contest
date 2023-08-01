n = int(input())
s = input()

win_num = (n + 2 - 1) // 2
t_cnt = 0
a_cnt = 0

for c in s:
    if c == 'T':
        t_cnt += 1
        if t_cnt == win_num:
            ans = 'T'
            break
    else:
        a_cnt += 1
        if a_cnt == win_num:
            ans = 'A'
            break

print(ans)
