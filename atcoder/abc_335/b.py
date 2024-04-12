n = int(input())
li = []
for x in range(n+1):
    for y in range(n+1):
        for z in range(n+1):
            if x + y + z <= n:
                li.append([x, y, z])

li.sort()
for i in li:
    print(*i)
