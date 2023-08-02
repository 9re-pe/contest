from collections import defaultdict

n = int(input())
q = int(input())

# key:box_num
box = defaultdict(list)
# key:card_num
card = defaultdict(set)

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        i, j = query[1], query[2]
        box[j].append(i)
        card[i].add(j)
    elif query[0] == 2:
        i = query[1]
        print(*sorted(box[i]))
    else:
        i = query[1]
        print(*sorted(card[i]))
