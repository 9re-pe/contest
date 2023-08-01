import itertools

n, m = map(int, input().split())
s = [input() for _ in range(n)]

t_list = list(itertools.permutations(s))
ans = 'No'
for t in t_list:
    this_t_ok = True
    for i in range(n-1):
        cnt = 0
        for j in range(m):
            if t[i][j] != t[i+1][j]:
                cnt += 1
        if cnt > 1:
            this_t_ok = False
    if this_t_ok:
        ans = 'Yes'

print(ans)
