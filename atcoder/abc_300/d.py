from math import sqrt, floor


def sieve_of_eratosthenes(limit):
    """
    2~limitまでの素数の昇順リストを取得
    """
    sieve = [True] * (limit + 1)
    sieve[0], sieve[1] = False, False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit + 1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]


n = int(input())
c_max = 3 * 10 ** 5
prime = sieve_of_eratosthenes(c_max)
n_prime = len(prime)
cnt = 0
flg = False
for i in range(n_prime):
    a = prime[i]
    x = a
    if x > n:
        break
    x *= a
    if x > n:
        break
    for j in range(i+1, n_prime):
        b = prime[j]
        x = a ** 2 * b
        if x > n:
            break
        for k in range(j+1, n_prime):
            c = prime[k]
            x = a ** 2 * b * c
            if x > n:
                break
            x *= c
            if x > n:
                break
            cnt += 1

print(cnt)
