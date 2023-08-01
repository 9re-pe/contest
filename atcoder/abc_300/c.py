h, w = map(int, input().split())
n = min(h, w)
s = [0] * n

c = [list(input()) for _ in range(h)]

for i in range(h):
    for j in range(w):
        d = 1
        while True:
            if c[i][j] == '#' and i+d < h and j+d < w and i-d >= 0 and j-d >= 0 and c[i+d][j+d] == '#' and c[i+d][j-d] == '#' and c[i-d][j+d] == '#' and c[i+d][j+d] == '#':
                d += 1
            else:
                break
        if d > 1:
            s[d-2] += 1

print(*s)
