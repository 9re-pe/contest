from collections import defaultdict

h, w = map(int, input().split())
s_dic = defaultdict(int)
t_dic = defaultdict(int)

s = [list(input()) for _ in range(h)]
t = [list(input()) for _ in range(h)]


for j in range(w):
    s_col = []
    t_col = []
    for i in range(h):
        s_col.append(s[i][j])
        t_col.append(t[i][j])
    s_dic[tuple(s_col)] += 1
    t_dic[tuple(t_col)] += 1

if s_dic == t_dic:
    print('Yes')
else:
    print('No')
