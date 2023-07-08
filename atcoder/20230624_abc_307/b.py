# 回文判定
def is_palindrome(string):
    # 文字列を逆順にして比較する
    reversed_string = string[::-1]

    # 元の文字列と逆順の文字列を比較して回文かどうかを判定する
    if string == reversed_string:
        return True
    else:
        return False


# 入力
n = int(input())
sn = [input() for _ in range(n)]

# 全探索
ans = False
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        # 回文判定
        if is_palindrome(sn[i] + sn[j]):
            ans = True

if ans:
    print('Yes')
else:
    print('No')
