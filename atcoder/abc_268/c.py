n = int(input())
p = list(map(int, input().split()))

# n:回転パターン
happy = [0] * n

for i in range(n):
    # mid回転したらちょうど人iの正面に行く
    mid = (p[i] - i) % n
    left = (mid - 1) % n
    right = (mid + 1) % n

    happy[mid] += 1
    happy[left] += 1
    happy[right] += 1

print(max(happy))
