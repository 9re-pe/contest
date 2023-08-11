n = int(input())
s = list(input())

in_kakko = False
for i in range(n):
    if s[i] == '"':
        if in_kakko:
            in_kakko = False
        else:
            in_kakko = True
    if s[i] == ',':
        if not in_kakko:
            s[i] = '.'

print(''.join(s))
