s = input()
cnt = 0
for c in s:
    if c == 'v':
        cnt += 1
    else:
        cnt += 2
print(cnt)
