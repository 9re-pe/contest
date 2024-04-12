n, q = map(int, input().split())
head_pos = [(1, 0)]
ans = []
for _ in range(q):
    t, x = tuple(input().split())
    if t == "1":
        if x == "R":
            head_pos.append((head_pos[-1][0] + 1, head_pos[-1][1]))
        if x == "L":
            head_pos.append((head_pos[-1][0] - 1, head_pos[-1][1]))
        if x == "U":
            head_pos.append((head_pos[-1][0], head_pos[-1][1] + 1))
        if x == "D":
            head_pos.append((head_pos[-1][0], head_pos[-1][1] - 1))
    if t == "2":
        x = int(x)
        if len(head_pos) >= x:
            ans.append(head_pos[-x])
        else:
            ans.append((head_pos[0][0] + (x - len(head_pos)), 0))
for i in ans:
    print(*i)
