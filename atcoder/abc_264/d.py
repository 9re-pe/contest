c2i = {
    'a': 0,
    't': 1,
    'c': 2,
    'o': 3,
    'd': 4,
    'e': 5,
    'r': 6
}
n = 7
s = input()
a = [c2i[c] for c in s]

ans = 0
for i in range(n-1):
    for j in range(n-1, i, -1):
        if a[j-1] > a[j]:
            a[j-1], a[j] = a[j], a[j-1]
            ans += 1
print(ans)
