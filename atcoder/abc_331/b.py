n, s, m, l = map(int, input().split())

INF = 10 ** 10
min_cost = INF

# すべての組み合わせを試す
for a in range(n // 6 + 2):
    for b in range(n // 8 + 2):
        for c in range(n // 12 + 2):
            if a * 6 + b * 8 + c * 12 >= n:
                cost = a * s + b * m + c * l
                min_cost = min(min_cost, cost)

print(min_cost)
