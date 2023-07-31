# 文字列が1文字違いかどうかを判別
def is_almost_equal(str1, str2):
    cnt = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            cnt += 1
            if cnt >= 2:
                break
    if cnt == 1:
        return True
    else:
        return False

# 入力
n, m = map(int, input().split())
str_list = [input() for _ in range(n)]

# 他の文字列とalmost equalになる文字列が1文字もない文字列があった場合No
ans = True
for str1 in str_list:
    cnt = 0
    for str2 in str_list:
        if is_almost_equal(str1, str2):
            cnt += 1
    if cnt == 0:
        ans = False

if ans:
    print('Yes')
else:
    print('No')
