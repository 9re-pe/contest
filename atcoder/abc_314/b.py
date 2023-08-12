n = int(input())
c_li = []
a_li = []
for _ in range(n):
    c = int(input())
    a = set(map(int, input().split()))
    c_li.append(c)
    a_li.append(a)
x = int(input())

ans = []
min_bet = 40
for i in range(n):
    if x in a_li[i]:
        if min_bet == c_li[i]:
            ans.append(i+1)
        elif min_bet > c_li[i]:
            ans = [i+1]
            min_bet = c_li[i]

print(len(ans))
print(*ans)

