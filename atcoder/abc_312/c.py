n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

b_plus = [i + 1 for i in b]
x_list = list({1} | set(a) | set(b_plus))
x_list.sort()

sale = 0
buy = len(b)
a_cnt = 0
b_cnt = 0
for x in x_list:

    while a_cnt < len(a) and a[a_cnt] <= x:
        sale += 1
        a_cnt += 1

    while b_cnt < len(b) and b[b_cnt] < x:
        buy -= 1
        b_cnt += 1

    if sale >= buy:
        print(x)
        break
