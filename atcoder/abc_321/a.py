n = list(input())

if len(n) == 1:
    print('Yes')
    exit(0)

ans = 'Yes'
for i in range(1, len(n)):
    if int(n[i-1]) <= int(n[i]):
        ans = 'No'
        break
print(ans)
