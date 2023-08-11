s = input()
n = len(s)

if n != 8:
    print('No')
    exit(0)

for i in range(n):
    if i == 0 or i == n-1:
        if s[i].isdigit():
            print('No')
            exit(0)
    elif i == 1:
        if s[i].isalpha() or s[i] == '0':
            print('No')
            exit(0)
    else:
        if s[i].isalpha():
            print('No')
            exit(0)

print('Yes')
