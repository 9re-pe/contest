n = int(input())
s = input()

for i in range(1, n):
    max_l = 0
    for k in range(n):
        if k+i <= n-1 and s[k] != s[k+i]:
            max_l = k + 1
        else:
            break
    print(max_l)
