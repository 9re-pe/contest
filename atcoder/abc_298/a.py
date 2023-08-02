n = int(input())
s = input()
s = set(list(s))

if 'o' in s and 'x' not in s:
    print('Yes')
else:
    print('No')
