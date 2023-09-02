"""O(NlogN)だけどTLE"""

n = int(input())
s = list(input())
w = list(map(int, input().split()))

combined = list(zip(w, s))
combined.sort()

w, test = zip(*combined)
test = int(''.join(test), 2)

# 連長圧縮的な
# w = [1, 2, 3, 4, 5] -> x = [1, 1, 1, 1, 1]
# w = [1, 1, 1, 2, 2] -> x = [3, 2]
x = []
cnt = 1
for i in range(1, n):
    if w[i] == w[i-1]:
        cnt += 1
    else:
        x.append(cnt)
        cnt = 1
x.append(cnt)

# xの累積和
t = [0]
for i in x:
    t.append(t[-1] + i)

ans = 0
for i in t:
    # これだとO(N)
    # hat = '0' * i + '1' * (n-i)
    # hat = int(hat, 2)

    # これだとO(1)
    hat = (1 << (n - i)) - 1

    diff_bits = test ^ hat
    collect = n - bin(diff_bits).count('1')

    ans = max(ans, collect)

print(ans)
