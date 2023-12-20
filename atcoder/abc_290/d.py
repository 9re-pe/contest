"""
- NとDが互いに素だと被らない
- 被る時は0でかぶる
- 被らない時，i番目に埋まるのは i * D % N
- ブロック単位でみる
    - 何番目のブロックか
    - ブロックの中で何番目か
"""


from math import gcd


t = int(input())
for _ in range(t):
    n, d, k = map(int, input().split())
    k -= 1
    g = gcd(n, d)
    m = n // g
    e = d // g
    b = (k * e) % m   # 何番目のブロックあk
    i = k // m        # ブロックの中で何番目か
    ans = b * g + i
    print(ans)


