from collections import deque


n, m = map(int, input().split())
s = list(input())
c = list(map(int, input().split()))

# 各色の文字の位置を保持する辞書を初期化
positions = {i: deque() for i in range(1, m+1)}

# c リストを使用して、各色の文字の位置を positions に追加
for i in range(n):
    positions[c[i]].append(i)

# 各色に対して巡回シフトを実行
for i in range(1, m+1):
    positions[i].appendleft(positions[i].pop())

# 文字列を構築
ans = ''
for color in c:
    ans += s[positions[color].popleft()]

# 結果を出力
print(ans)
