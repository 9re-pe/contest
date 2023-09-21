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
p = sieve_of_eratosthenes(10**6)
len_p = len(p)

ans = 0
# 尺取り法
k = len_p-1
for i in range(len_p):
    # p: i番目の素数(固定する変数)
    # q: k番目の素数
    # p*q^3<=Nとなるまでkを減らしていく
    while 0 < k and n < p[i] * p[k]**3:
        k -= 1

    if k <= i:
        break

    ans += k - i

print(ans)
