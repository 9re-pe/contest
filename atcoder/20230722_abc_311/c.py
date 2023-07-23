import sys
sys.setrecursionlimit(10**6)


def dfs(now):
    global s
    global visited
    global mini_graph

    # 終了条件
    if visited[now] == 1:
        s = now
        return

    visited[now] = 1
    mini_graph.append(now)
    dfs(graph[now])


n = int(input())
graph = [-1]
graph += list(map(int, input().split()))
visited = [0] * (n+1)

mini_graph = []
s = 0
dfs(1)
li = mini_graph[mini_graph.index(s):]

print(len(li))
print(*li)
