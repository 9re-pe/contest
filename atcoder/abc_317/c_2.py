"""bit全探索"""


from itertools import permutations


n, m = map(int, input().split())
graph = [[0] * n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    graph[a][b] = c
    graph[b][a] = c

ans = 0
# 各街を通るor通らないでbit全探索
for mask in range(1 << n):
    # 通る街のリスト
    cities = [i for i in range(n) if (mask >> i) & 1]

    # 全ての通過順について距離を計算
    for perm in permutations(cities):
        distance = 0
        valid = True  # そのルートが実現可能か
        for i in range(len(perm)-1):
            if graph[perm[i]][perm[i+1]] == 0:
                valid = False
                break
            distance += graph[perm[i]][perm[i+1]]
        if valid:
            ans = max(ans, distance)

print(ans)
