r, c, = map(int, input().split())
b = [list(input()) for _ in range(r)]

for i in range(r):
    for j in range(c):
        if b[i][j] == '.' or b[i][j] == '#':
            continue
        else:
            power = int(b[i][j])
            for k in range(max(0, i-power), min(r, i+power+1)):
                for l in range(max(0, j-power), min(c, j+power+1)):
                    if abs(k-i) + abs(l-j) <= power and b[k][l] == '#':
                        b[k][l] = '.'
            b[i][j] = '.'

for i in range(r):
    print(''.join(map(str, b[i])))
