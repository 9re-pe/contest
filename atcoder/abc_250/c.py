n, q = map(int, input().split())
a = [-1] + [i for i in range(1, n + 1)]
pos_dict = {i: i for i in range(1, n + 1)}

for _ in range(q):
    x = int(input())

    # 右端の場合
    if pos_dict[x] == n:
        pos = pos_dict[x]
        next_num = a[pos - 1]

        a[pos], a[pos - 1] = a[pos - 1], a[pos]
        pos_dict[x], pos_dict[next_num] = pos_dict[next_num], pos_dict[x]

    else:
        pos = pos_dict[x]
        next_num = a[pos + 1]

        a[pos], a[pos + 1] = a[pos + 1], a[pos]
        pos_dict[x], pos_dict[next_num] = pos_dict[next_num], pos_dict[x]

print(*a[1:])
