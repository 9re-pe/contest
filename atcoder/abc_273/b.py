x, k = map(int, input().split())
for i in range(k):
    digit = 10 ** (i+1)
    offset = 5 * (digit // 10)
    x = ((x + offset) // digit) * digit

print(x)
