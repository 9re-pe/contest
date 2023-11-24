from collections import defaultdict


s = input()
n = len(s)

table = [[0] * 10 for _ in range(n+1)]

for i in range(n):
    c = int(s[i])
    table[i+1] = table[i].copy()
    table[i+1][c] = (table[i][c] + 1) % 2

dic = defaultdict(int)
for i in range(n+1):
    dic[tuple(table[i])] += 1

ans = 0
for v in dic.values():
    ans += v * (v-1) // 2

print(ans)
