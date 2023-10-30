import itertools


INF = 10 ** 9
m = int(input())

s = []
for _ in range(3):
    si = input()
    s.append(si + si)

orders = list(itertools.permutations(range(3)))


def solve(order, num):
    for si in s:
        if num not in si:
            return 10 ** 9
    crr = 0
    for reel in order:
        crr += s[reel][crr % m:].index(num)+1
    return crr - 1


ans = INF
for num in range(10):
    for order in orders:
        ans = min(ans, solve(order, str(num)))

print(ans if ans != INF else -1)
