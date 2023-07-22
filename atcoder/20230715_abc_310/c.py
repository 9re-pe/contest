n = int(input())
s = [input() for _ in range(n)]
ans = set()

for si in s:
    si_rev = ''.join(list(reversed(list(si))))
    if si not in ans and si_rev not in ans:
        ans.add(si)

print(len(ans))
