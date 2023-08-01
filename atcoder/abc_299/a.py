n = int(input())
s = input()

status = 0
for i in range(n):
    if s[i] == '|':
        status += 1
    if s[i] == '*':
        if status == 1:
            print('in')
        else:
            print('out')
