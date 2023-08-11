s = input()

cnt = 0
skip = False
for i in range(len(s)):
    if skip:
        skip = False
        continue

    if s[i] == '0' and i+1 <= len(s)-1 and s[i+1] == '0':
        skip = True

    cnt += 1

print(cnt)
