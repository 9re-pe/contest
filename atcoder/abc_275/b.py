mod = 998244353
a, b, c, d, e, f = map(int, input().split())

a %= mod
b %= mod
c %= mod
d %= mod
e %= mod
f %= mod

abc = (a*b*c) % mod
_def = (d*e*f) % mod

print((abc-_def) % mod)
