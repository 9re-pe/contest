n = int(input())
ij2num = dict()

for i in range(n):
    row = input()
    for j in range(n):
        ij2num[(i, j)] = row[j]

directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0,  -1),          (0,  1),
    (1,  -1), (1,  0), (1,  1)
]

ans = 0
for i in range(n):
    for j in range(n):
        for direction in directions:
            cur = [i, j]
            num = ij2num[(i, j)]
            for _ in range(n-1):
                cur[0] = (cur[0] + direction[0]) % n
                cur[1] = (cur[1] + direction[1]) % n
                num += ij2num[tuple(cur)]
            ans = max(ans, int(num))

print(ans)
