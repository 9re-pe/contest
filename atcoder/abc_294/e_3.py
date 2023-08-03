L, n1, n2 = map(int, input().split())
v1 = [0] * n1
L1 = [0] * (n1 + 1)
for i in range(n1):
    v1[i], L1[i] = map(int, input().split())
v2 = [0] * n2
L2 = [0] * (n2 + 1)
for i in range(n2):
    v2[i], L2[i] = map(int, input().split())

# 解答
ans = 0
# いま見ているマス目
cur_pos = 0
# 参照している連長圧縮データのインデックス
cur_n1 = 0
cur_n2 = 0
# 連長圧縮データの境目までの距離
remain_n1 = L1[0]
remain_n2 = L2[0]
"""
1. 小さい方の境目までcur_posを進める
2. 色が同じか判定
3. remain_n1,2の更新
"""
while cur_pos < L:
    if remain_n1 < remain_n2:
        cur_pos += remain_n1
        if v1[cur_n1] == v2[cur_n2]:
            ans += remain_n1
        remain_n2 -= remain_n1
        cur_n1 += 1
        remain_n1 = L1[cur_n1]
    elif remain_n1 > remain_n2:
        cur_pos += remain_n2
        if v1[cur_n1] == v2[cur_n2]:
            ans += remain_n2
        remain_n1 -= remain_n2
        cur_n2 += 1
        remain_n2 = L2[cur_n2]
    else:
        cur_pos += remain_n1
        if v1[cur_n1] == v2[cur_n2]:
            ans += remain_n1
        cur_n1 += 1
        remain_n1 = L1[cur_n1]
        cur_n2 += 1
        remain_n2 = L2[cur_n2]

print(ans)
