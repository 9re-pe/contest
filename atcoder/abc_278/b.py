def is_misjudge_time(h, m):
    h = "{:02}".format(h)
    m = "{:02}".format(m)

    return 0 <= int(h[0]+m[0]) <= 23 and 0 <= int(h[1]+m[1]) <= 59


h, m = map(int, input().split())

while True:
    if is_misjudge_time(h, m):
        print(h, m)
        break

    m += 1
    if m == 60:
        h += 1
        m = 0
        if h == 24:
            h = 0
