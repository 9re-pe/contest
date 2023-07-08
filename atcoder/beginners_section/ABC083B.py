n, a, b = map(int, input().split())

ans = 0
for i in range(1, n + 1):
    # 10の整数を文字列に変換する
    i_str = str(i)
    sum = 0
    for j_str in list(i_str):
        j = int(j_str)
        sum += j
        # 上限の判定はここでやったほうがはやい?
    if (a <= sum and sum <= b):
        ans += i

print(ans)
