def dfs(now):
    global n, t, teams, ans

    # 終了条件
    if now == n:
        # 判定処理
        if len(teams) == t:
            ans += 1
        return

    # 既存のチームに追加
    for i in range(len(teams)):
        # teams[i]に追加していいか判定
        can_add = True
        for member in teams[i]:
            if ng[now][member]:
                can_add = False
        # teams[i]に追加
        if can_add:
            teams[i].append(now)
            dfs(now + 1)
            # 一つ前の状態に戻す
            teams[i].pop(-1)
    # 新しいチームとして追加
    if len(teams) < t:
        teams.append([now])
        dfs(now + 1)
        # 一つ前の状態に戻す
        teams.pop(-1)


n, t, m = map(int, input().split())
ng = [[False for j in range(n)] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    ng[a-1][b-1] = True
    ng[b-1][a-1] = True

teams = []
ans = 0

dfs(0)
print(ans)
