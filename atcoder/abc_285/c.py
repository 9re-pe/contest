s = input()

# 文字を1~26の整数に変換
d = []
c2int = {chr(i+65): i+1 for i in range(26)}
for c in s:
    d.append(c2int[c])

# 進数変換
ans = 0
for i in range(len(d)):
    ans += 26**i * d[-i-1]

print(ans)
