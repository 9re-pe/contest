property_num = 10**19

n = int(input())

ratio = []
for i in range(n):
    ai, bi = map(int, input().split())
    ratio.append([property_num*ai // (ai+bi), -(i+1)])

ratio.sort(reverse=True)

ans = []
for i in range(n):
    ans.append(-ratio[i][1])
print(*ans)
