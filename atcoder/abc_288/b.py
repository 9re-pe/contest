n, k = map(int, input().split())

s = []
for _ in range(n):
    s.append(input())

top_k = s[:k]
top_k.sort()
for i in range(k):
    print(top_k[i])
