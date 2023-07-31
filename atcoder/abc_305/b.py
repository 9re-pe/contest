# Aからその文字までの距離を定義しておく(手計算)
dic = {
    'A': 0,
    'B': 3,
    'C': 4,
    'D': 8,
    'E': 9,
    'F': 14,
    'G': 23
}

x, y = input().split()

if x < y:
    ans = dic[y] - dic[x]
else:
    ans = dic[x] - dic[y]

print(ans)

