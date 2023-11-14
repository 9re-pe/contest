n, q = map(int, input().split())
s = input()

pairs = [0] * n
for i in range(1, n):
    pairs[i] = pairs[i - 1] + (s[i] == s[i - 1])

for _ in range(q):
    l, r = map(int, input().split())
    print(pairs[r - 1] - pairs[l - 1])
