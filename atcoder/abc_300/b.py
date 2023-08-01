import copy

h, w = map(int, input().split())
a = [list(input()) for _ in range(h)]
b = [list(input()) for _ in range(h)]

ans = 'No'
for s in range(h):
    for t in range(w):
        a_cp = copy.deepcopy(a)
        # 縦方向のシフト
        for _ in range(s):
            tmp = a_cp[0]
            for i in range(h-1):
                a_cp[i] = a_cp[i+1]
            a_cp[h-1] = tmp
        # 横方向のシフト
        for _ in range(t):
            for i in range(h):
                tmp = a_cp[i][0]
                for j in range(w-1):
                    a_cp[i][j] = a_cp[i][j+1]
                a_cp[i][w-1] = tmp

        if a_cp == b:
            ans = 'Yes'

print(ans)
