n, m = map(int, input().split())

s3s = []
for _ in range(n):
    s = input()
    s3s.append(s[-3:])

t = set()
for _ in range(m):
    t.add(input())

cnt = 0
for s3 in s3s:
    if s3 in t:
        cnt += 1

print(cnt)
