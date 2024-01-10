a, m, l, r = map(int, input().split())

k_left = (l - a + m - 1) // m
k_right = (r - a) // m

print(k_right - k_left + 1)
