n, m = map(int, input().split())
s = list(input())
t = list(input())

prefix = False
if t[:n] == s:
    prefix = True

suffix = False
if t[-n:] == s:
    suffix = True

if prefix and suffix:
    print(0)
elif prefix and not suffix:
    print(1)
elif not prefix and suffix:
    print(2)
else:
    print(3)
