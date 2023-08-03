import string

h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
code_map = ['.'] + list(string.ascii_uppercase)
ans = mt = [[0 for j in range(w)] for i in range(h)]

for i in range(h):
    for j in range(w):
        ans[i][j] = code_map[a[i][j]]

for i in range(h):
    print(''.join(map(str, ans[i])))
