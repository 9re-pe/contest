import itertools

n, m = map(int, input().split())
s = []
for _ in range(n):
    s.append(input())
all_pairs = list(itertools.combinations(range(n), 2))

cnt = 0
for pair in all_pairs:
    ok = True
    for i in range(m):
        if s[pair[0]][i] == 'x' and s[pair[1]][i] == 'x':
            ok = False
            break
    if ok:
        cnt += 1

print(cnt)
