def get_j(x):
    global n
    global a

    left = 0
    right = n-1

    while right - left > 1:
        center = (left + right) // 2

        if a[center] < x:
            left = center
        else:
            right = center

    return left


def f(x):
    global fa

    j = get_j(x)

    return fa[j] + (fa[j+1] - fa[j]) * (x - a[j]) // (a[j+1] - a[j])


n = int(input())
a = list(map(int, input().split()))

fa = [0] * n
for i in range(n):
    if i == 0:
        fa[i] = 0
    elif i % 2 == 0:
        fa[i] = fa[i-1] + (a[i] - a[i-1])
    else:
        fa[i] = fa[i-1]

q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    print(f(r) - f(l))

