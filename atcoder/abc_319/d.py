def judge(w):
    # w = 横幅制限値
    # return : 横幅w以内の制限のもとm行に収められるか

    # その行の現在の文字数
    n_chr = 0
    # 行数
    n_row = 1

    for i in range(n):
        # はみ出るときは改行して追加
        if n_chr + l[i] > w:
            n_row += 1
            n_chr = l[i] + 1
        # はみ出さない時は現在の行に追加
        else:
            n_chr += l[i] + 1

    return n_row <= m


n, m = map(int, input().split())
l = list(map(int, input().split()))

# 1単語ずつ改行したときの横幅
left = max(l) - 1
# 全てを1行に配置した場合の横幅
right = sum(l) + n
while right - left > 1:
    mid = (left + right) // 2
    # 横幅midでm行に収まるならもっと狭くしてみる
    if judge(mid):
        right = mid
    # 横幅midでm行に治らないならもっと秘匿してみる
    else:
        left = mid

print(right)
