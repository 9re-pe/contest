s = input()
t = input()
n = len(s)

for i in range(n):
    if s[i] != t[i]:
        print(i+1)
        exit(0)

print(n+1)
