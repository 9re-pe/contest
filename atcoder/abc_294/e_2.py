l, n1, n2 = map(int, input().split())
grid = [[0 for j in range(l)] for i in range(2)]

s = 0
for _ in range(n1):
    num, length = map(int, input().split())
    for i in range(length):
        grid[0][s+i] = num
    s = s + length

s = 0
for _ in range(n2):
    num, length = map(int, input().split())
    for i in range(length):
        grid[1][s+i] = num
    s = s + length

ans = 0
for j in range(l):
    if grid[0][j] == grid[1][j]:
        ans += 1

print(ans)
