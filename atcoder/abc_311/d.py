import sys
sys.setrecursionlimit(10**9)


DIRECTIONS = [
    (0, 1),   # 上
    (0, -1),  # 下
    (1, 0),   # 右
    (-1, 0)   # 左
]


def dfs(u):
    # 元の位置に止まったら終了
    if stopped[u[0]][u[1]] == 1:
        return

    stopped[u[0]][u[1]] = 1

    for d in DIRECTIONS:
        v = move(u, d)
        dfs(v)


def move(u, d):
    """
    移動したマスのvisitedを1にし、終了地点を返す
    :param u: 移動開始地点
    :param d: 移動方向
    :return: 終了地点
    """
    v = u
    while True:
        visited[v[0]][v[1]] = 1
        nxt = tuple(x + y for x, y in zip(v, d))

        # 移動方向の先にあるマスが岩なら終了
        if grid[nxt[0]][nxt[1]] == '#':
            break

        v = nxt

    return v


n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
stopped = [[0] * m for _ in range(n)]
dfs((1, 1))
ans = 0
for row in visited:
    ans += sum(row)
print(ans)
