"""TLE and MLE"""


n = int(input())
s = input()

checked = set()
tmp = ''
for i in range(n):
    if i == 0:
        tmp = s[i]
    elif tmp[-1] == s[i]:
        tmp += s[i]
    else:
        tmp = s[i]

    checked.add(tmp)

print(len(checked))
