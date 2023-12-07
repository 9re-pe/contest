n, s, m, l = map(int, input().split())

INF = 10 ** 10
min_cost = INF

# すべての組み合わせを試す
for a in range(n // 6 + 2):
    for b in range(n // 8 + 2):
        for c in range(n // 12 + 2):
            # 卵の合計数がN個以上かどうかを確認
            if a * 6 + b * 8 + c * 12 >= n:
                # コストを計算
                cost = a * s + b * m + c * l
                # 最小コストを更新
                min_cost = min(min_cost, cost)

print(min_cost)
