# 入力の受け取り
N = int(input())

# 区間の情報を格納するリスト
LR = []

# N回
for i in range(N):
    # 入力の受け取り
    L, R = map(int, input().split())
    # 区間の情報を格納
    LR.append([L, R])

# 左側の小さい順にソート
LR.sort()

# 今の区間左側
NowL = LR[0][0]
# 今の区間右側
NowR = LR[0][1]

# i=1~(N-1)
for i in range(1, N):
    # 次の(i番目の)区間左側
    NextL = LR[i][0]
    # 次の(i番目の)区間右側
    NextR = LR[i][1]

    # 「今の右側」<「次の左側」
    if NowR < NextL:
        # [NowL,NowR)は絶対に必要な区間
        print(NowL, NowR)
        # 今の区間を更新
        NowL = NextL
        NowR = NextR

    # それ以外(「次の左側」≤「今の右側」)
    else:
        # 「今の右側」<「次の右側」
        if NowR < NextR:
            # 区間を更新(右側を広げる)
            NowR = NextR

# 最後に区間を出力
print(NowL, NowR)
