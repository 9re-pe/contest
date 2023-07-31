import itertools

# 入力
n, m = map(int, input().split())
row_list = []
for i in range(m):
    row_list.append(list(map(int, input().split())))

cnt = 0
all_pair = list(itertools.combinations(range(1, n+1), 2))
for pair in all_pair:
    is_friends = False
    for row in row_list:
        for i in range(n-1):
            if (row[i], row[i+1]) == pair:
                is_friends = True
            elif ((row[i], row[i+1])) == (pair[1], pair[0]):
                is_friends = True
    if not is_friends:
        cnt += 1

# 出力
print(cnt)