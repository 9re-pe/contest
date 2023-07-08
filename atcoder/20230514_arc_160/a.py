# f
def f (an, l, r):
    reverse_range_list = list(reversed(an[l-1:r]))
    re = an[:l-1] + reverse_range_list + an[r:]

    return re

# 大きさの同じ数列同士の大小関係を比較する
# anがbnより小さればtrueを返す
# def an_is_smaller_than_bn (an, bn):
#     for i in range(len(an)):
#         if an[i] == bn[i]:
#             continue
#         return an[i] < bn[i]

# 入力
n, k = map(int, input().split())
an = list(map(int, input().split()))

an_list = []
for l in range(1, n + 1):
    for r in range(l, n + 1):
        reversed_an = f(an, l, r)
        #print('f({}, {}) = {}'.format(l, r, reversed_an))
        # ソートしながら追加していく    
        if len(an_list) == 0:
            # 最初の数列のときはそのまま追加
            an_list.append(reversed_an)
        else:
            # 自分が入る場所を小さい方から見つける
            for i in range(len(an_list)):
                # kよりでかいところは考えなくて良い
                if len(an_list) > k:
                    if an_list[k - 1] < reversed_an:
                        continue
                # 自分より大きい要素を見つけたら挿入
                if reversed_an < an_list[i]:
                    an_list.insert(i, reversed_an)
                    break
                # 見つからなかった場合(自分が一番大きい)場合は末尾に追加
                if i == len(an_list) - 1:
                    an_list.append(reversed_an)
        #print(an_list)

# 出力
ans = an_list[k - 1]
print(*ans)
