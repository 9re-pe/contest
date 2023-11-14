s = input()
ans = []
for c in s:
    if ans[-2:] == ['A', 'B'] and c == 'C':
        ans.pop()
        ans.pop()
    else:
        ans.append(c)
print(''.join(ans))
