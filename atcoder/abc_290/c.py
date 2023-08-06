n, k = map(int, input().split())
a = list(map(int, input().split()))

# 重複削除
a = set(a)
a = list(a)

a.sort()

if a[0] != 0:
    print(0)
    exit(0)

# 0からどこまで連番になっているか調べる
# 連番の末尾であるべき数
last = 0
for i in range(len(a)):
    if a[i] == last:
        last += 1
    else:
        break

if last >= k:
    print(k)
else:
    # +1された状態で終わっているので
    print(last)
