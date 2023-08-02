s = input()

b1 = -1
b2 = -1
r1 = -1
r2 = -1
k  = -1
for i in range(8):
    if s[i] == 'B':
        if b1 == -1:
            b1 = i
        else:
            b2 = i
    elif s[i] == 'R':
        if r1 == -1:
            r1 = i
        else:
            r2 = i
    elif s[i] == 'K':
        k = i

if b1 % 2 != b2 % 2 and r1 < k < r2:
    print('Yes')
else:
    print('No')

