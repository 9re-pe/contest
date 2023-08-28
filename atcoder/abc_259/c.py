s = input()
t = input()
ns = len(s)
nt = len(t)

s_cnt = 0
t_cnt = 0
ans = 'Yes'
while True:
    if s_cnt > ns-1 and t_cnt > nt-1:
        break

    if s_cnt > ns-1 and t_cnt <= nt-1:
        if s_cnt-2 >= 0 and s[s_cnt-1] == t[t_cnt] and s[s_cnt-1] == s[s_cnt-2]:
            t_cnt += 1
            continue
        else:
            ans = 'No'
            break

    if s_cnt <= ns-1 and t_cnt > nt-1:
        ans = 'No'
        break

    if s[s_cnt] == t[t_cnt]:
        s_cnt += 1
        t_cnt += 1
        continue

    if s_cnt-2 >= 0 and s[s_cnt-1] == t[t_cnt] and s[s_cnt-1] == s[s_cnt-2]:
        t_cnt += 1
        continue

    ans = 'No'
    break

print(ans)
