n = int(input())
q = n // 5
r = n % 5

if r <= 2:
    ans = q * 5
else:
    ans = (q + 1) * 5

print(ans)
