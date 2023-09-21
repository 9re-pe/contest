import math


def sigma_1_to_n(n):
    return (1 + n) * n // 2


def sigma_skip_x(x):
    to = n // x
    return x * sigma_1_to_n(to)


n, a, b = map(int, input().split())
lcm = abs(a * b) // math.gcd(a, b)

print(sigma_1_to_n(n) - sigma_skip_x(a) - sigma_skip_x(b) + sigma_skip_x(lcm))
