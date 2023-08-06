n, m = map(int, input().split())
one2n = set([i + 1 for i in range(n)])

a_li = []
for _ in range(m):
    c = int(input())
    a = set(map(int, input().split()))
    a_li.append(a)

ans = 0
for num in range(1 << m):
    union = set()
    cnt = 0

    for shift in range(m):
        # shift番目を選ぶ
        if 1 & num >> shift == 1:
            union |= a_li[shift]
            cnt += 1

    # 少なくとも1つ選ぶ
    if cnt == 0:
        continue

    # 1~nの全ての要素を持つか判定
    if one2n.issubset(union):
        ans += 1

print(ans)
