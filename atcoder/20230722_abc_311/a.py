n = int(input())
s = list(input())

a_flg = False
b_flg = False
c_flg = False
ans = -1
for i in range(n):
    if s[i] == 'A':
        a_flg = True
    elif s[i] == 'B':
        b_flg = True
    elif s[i] == 'C':
        c_flg = True

    if a_flg and b_flg and c_flg:
        ans = i+1
        break

print(ans)
