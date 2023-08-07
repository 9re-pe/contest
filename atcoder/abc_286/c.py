n, a, b = map(int, input().split())
s = list(input())

# 後半を前半に合わせたとき(適当なクソデカ数にしたらWAになった)
ans = n // 2 * b
for a_cnt in range(n):
    s_cp = s.copy()
    # 操作Aをi回行う
    s_cp = s_cp[a_cnt:] + s_cp[:a_cnt]

    # 外側から入れ替えて回文にしていく
    b_cnt = 0
    for j in range(n // 2):
        if s_cp[j] != s_cp[-j-1]:
            b_cnt += 1

    ans = min(ans, a * a_cnt + b * b_cnt)

print(ans)
