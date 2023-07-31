# 入力を2次元リストで受け取る
character_array = []
h, w = map(int, input().split())
for i in range(h):
    # 一文字づつ格納
    row = list(input())
    character_array.append(row)

# 探索
for i in range(h):
    for j in range(w):
        if character_array[i][j] == 's':
            # 横(左から右)に並んでいるとき
            if j + 4 <= w - 1 and character_array[i][j + 1] == 'n' and character_array[i][j + 2] == 'u' and character_array[i][j + 3] == 'k' and character_array[i][j + 4] == 'e':
                s_position = (i, j, 0)
            # 横(右から左)に並んでいるとき
            if j - 4 >= 0 and character_array[i][j - 1] == 'n' and character_array[i][j - 2] == 'u' and character_array[i][j - 3] == 'k' and character_array[i][j - 4] == 'e':
                s_position = (i, j, 1)
            # 縦(上から下)に並んでいるとき
            elif i + 4 <= h - 1 and character_array[i + 1][j] == 'n' and character_array[i + 2][j] == 'u' and character_array[i + 3][j] == 'k' and character_array[i + 4][j] == 'e':
                s_position = (i, j, 2)
            # 縦(下から上)に並んでいるとき
            elif i - 4 >= 0 and character_array[i - 1][j] == 'n' and character_array[i - 2][j] == 'u' and character_array[i - 3][j] == 'k' and character_array[i - 4][j] == 'e':
                s_position = (i, j, 3)
            # ななめ(左上から右下)にならんでいるとき
            elif j + 4 <= w - 1 and i + 4 <= h - 1 and character_array[i + 1][j + 1] == 'n' and character_array[i + 2][j + 2] == 'u' and character_array[i + 3][j + 3] == 'k' and character_array[i + 4][j + 4] == 'e':
                s_position = (i, j, 4)
            # ななめ(右下から左上)にならんでいるとき
            elif j - 4 >= 0 and i - 4 >= 0 and character_array[i - 1][j - 1] == 'n' and character_array[i - 2][j - 2] == 'u' and character_array[i - 3][j - 3] == 'k' and character_array[i - 4][j - 4] == 'e':
                s_position = (i, j, 5)
            # ななめ(右上から左下)にならんでいるとき
            elif j - 4 >= 0 and i + 4 <= h - 1 and character_array[i + 1][j - 1] == 'n' and character_array[i + 2][j - 2] == 'u' and character_array[i + 3][j - 3] == 'k' and character_array[i + 4][j - 4] == 'e':
                s_position = (i, j, 6)
            # ななめ(左下から右上)にならんでいるとき
            elif j + 4 <= w - 1 and i - 4 >= 0 and character_array[i - 1][j + 1] == 'n' and character_array[i - 2][j + 2] == 'u' and character_array[i - 3][j + 3] == 'k' and character_array[i - 4][j + 4] == 'e':
                s_position = (i, j, 7)

# 出力時はi, jに1足す
if s_position[2] == 0:
    for i in range(5):
        print('{} {}'.format(s_position[0] + 1, s_position[1] + 1 + i))
elif s_position[2] == 1:
    for i in range(5):
        print('{} {}'.format(s_position[0] + 1, s_position[1] + 1 - i))
elif s_position[2] == 2:
    for i in range(5):
        print('{} {}'.format(s_position[0] + 1 + i, s_position[1] + 1))
elif s_position[2] == 3:
    for i in range(5):
        print('{} {}'.format(s_position[0] + 1 - i, s_position[1] + 1))
elif s_position[2] == 4:
    for i in range(5):
        print('{} {}'.format(s_position[0] + 1 + i, s_position[1] + 1 + i))
elif s_position[2] == 5:
    for i in range(5):
        print('{} {}'.format(s_position[0] + 1 - i, s_position[1] + 1 - i))
elif s_position[2] == 6:
    for i in range(5):
        print('{} {}'.format(s_position[0] + 1 + i, s_position[1] + 1 - i))
elif s_position[2] == 7:
    for i in range(5):
        print('{} {}'.format(s_position[0] + 1 - i, s_position[1] + 1 + i))

    
