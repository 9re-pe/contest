from collections import deque

h, w = map(int, input().split())
grid = [list(input()) for _ in range(h)]
# 探索する方角
di_list = [('U', -1, 0), ('D', 1, 0), ('L', 0, -1), ('R', 0, 1)]
# 訪問済みの頂点
visited = [[0] * w for _ in range(h)]
# 最初は右下
que = deque([('D', 1, 1), ('R', 1, 1)])
# 探索したマスと方角を記録
searched = set()
visited[1][1] = 1

while que:
    # 方角、マス
    direction, r, c = que.popleft()
    # 探索済みだったらcontinue
    if (direction, r, c) in searched:
        continue
    searched.add((direction, r, c))
    for di in di_list:
        if di[0] == direction:
            nr = r
            nc = c
            # 範囲内を探す
            while 0 <= nr < h and 0 <= nc < w:
                nr += di[1]
                nc += di[2]
                if grid[nr][nc] == '.':
                    que.append((direction, nr, nc))
                    visited[nr][nc] = 1
                else:
                    # 岩にぶつかったので、一個戻って加える
                    # 上下に移動していた場合は左右、左右に移動していたら上下を次に加える
                    if direction == 'U' or direction == 'D':
                        ignore = 'UD'
                    else:
                        ignore = 'LR'
                    for char in 'UDLR':
                        if char in ignore:
                            continue
                        que.append((char, nr - di[1], nc - di[2]))
                    break

ans = 0
for al in visited:
    ans += sum(al)
print(ans)
