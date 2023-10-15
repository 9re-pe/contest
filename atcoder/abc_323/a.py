s = input()
for i in range(16):
    num = i + 1
    if num % 2 == 0 and s[i] == '1':
        print('No')
        break
else:
    print('Yes')

