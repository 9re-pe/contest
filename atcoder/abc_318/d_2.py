def dfs(used):
    if all(used):
        return 0

    # まだ使われてないノードをひとつ選択
    v = used.index(False)
    used[v] = True

    re = 0
    for w in range(v+1, n):
        # 上位のループで使われていなければ
        if not used[w]:
            used[w] = True
            re = max(re, d[v][w]+dfs(used))
            # ロールバック
            used[w] = False
    # ロールバック
    used[v] = False
    return re


n = int(input())
graph = [[0] * n for _ in range(n)]
for i in range(n-1):
    d = list(map(int, input().split()))
    for j in range(i+1, n):
        graph[i][j] = d[j-i-1]
        graph[j][i] = d[j-i-1]

used = [False] * n
ans = 0
if n % 2 == 0:
    ans = dfs(used)
else:
    # 使わないノードを1つ決める
    for v in range(n):
        used[v] = True
        ans = max(ans, dfs(used))
        used[v] = False

print(ans)
