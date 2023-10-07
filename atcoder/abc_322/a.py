n = int(input())
s = input()

a_flg = False
ab_flg = False
for i in range(n-2):
    if s[i] + s[i+1] + s[i+2] == 'ABC':
        print(i+1)
        break
else:
    print(-1)
