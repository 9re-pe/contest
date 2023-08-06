def eq(a, b):
    if a == b:
        return True
    if a == '?' or b == '?':
        return True

    return False


s = input()
t = input()
t_len = len(t)

dp = [[False, False] for _ in range(t_len+1)]
dp[0][0] = True
dp[t_len][1] = True
for i in range(1, t_len+1):
    dp[i][0] = dp[i-1][0] and eq(s[i-1], t[i-1])
    dp[t_len-i][1] = dp[t_len-i+1][1] and eq(s[-i], t[-i])

for x in range(t_len+1):
    if dp[x][0] and dp[x][1]:
        print('Yes')
    else:
        print('No')
