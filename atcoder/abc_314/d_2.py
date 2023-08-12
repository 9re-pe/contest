n = input()
s = list(input())
q = int(input())
query = [input().split() for _ in range(q)]

# クエリを先読みして最後の変換クエリのインデックスを取得しておく
last = -1
for i, (t, _, _) in enumerate(query):
    if t == '2' or t == '3':
        last = i

for i, (t, x, c) in enumerate(query):
    if t == '1':
        s[int(x)-1] = c
    elif t == '2':
        if i == last:
            s = list("".join(s).lower())
    else:
        if i == last:
            s = list("".join(s).upper())

print("".join(s))
