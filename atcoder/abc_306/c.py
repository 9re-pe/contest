n = int(input())
a = list(map(int, input().split()))

cnt = [0] * (n + 1)
ans = []

# i: 1~3Nの通し番号
# ai: 1~Nのどれかの数字
for ai in a:
    cnt[ai] += 1
    if cnt[ai] == 2:
        ans.append(ai)

print(*ans)

