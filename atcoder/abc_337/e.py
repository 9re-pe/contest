import sys


def find_spoiled_juice(N):
    # 必要な友人の数を計算
    num_friends = (N - 1).bit_length()

    # 友人ごとにジュースを割り当てる
    for i in range(num_friends):
        juices = [j for j in range(1, N + 1) if (j >> i) & 1]
        # ジュースが1本もない場合は、全てのジュースを割り当てる
        if not juices:
            juices = list(range(1, N + 1))
        print(len(juices), *juices)
        sys.stdout.flush()

    # ジャッジからの反応を受け取る
    response = input()

    # 腐ったジュースを特定
    spoiled_juice = 0
    for i in range(num_friends):
        if i < len(response) and response[i] == '1':
            spoiled_juice |= 1 << i

    # もし反応が全て0なら、腐ったジュースは最後の1本である
    if not any(char == '1' for char in response):
        spoiled_juice = N

    return spoiled_juice


# ジャッジからNを受け取る
N = int(input())
# 必要な友人の数を計算して出力
print((N - 1).bit_length())
# 腐ったジュースを特定して出力
print(find_spoiled_juice(N))
sys.stdout.flush()
