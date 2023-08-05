s = list(input())
n = len(s)

for i in range(n):
    if i % 2 == 0:
        tmp = s[i]
        s[i] = s[i+1]
        s[i+1] = tmp

print(''.join(map(str, s)))
