h, w = map(int, input().split())
cnt = 0
for _ in range(h):
    s = input()
    for j in range(w):
        if s[j] == '#':
            cnt += 1

print(cnt)
