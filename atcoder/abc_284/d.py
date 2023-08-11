from math import sqrt

# O(10^7)に納めたい
# p,qのどちらかは必ず10^7より小さい
t = int(input())
for _ in range(t):
    n = int(input())

    for x in range(2, 10**7+1):
        if n % x ** 2 == 0:
            print(x, n // x ** 2)
            break
        elif n % x == 0:
            print(int(sqrt(n // x)), x)
            break
