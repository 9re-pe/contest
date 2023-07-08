# 入力
X, Y, Z = map(int, input().split())
S = input()

# 動的計画法
time = 0
caps_lock = False
for s in S:
    # aを入力したいとき
    if s == 'a':
        # ONのとき
        if caps_lock:
            time1 = Y
            time2 = Z + X
            if time1 > time2:
                print('a')
                time += time1
            else:
                print('b')
                time += time2
                caps_lock = True
        # OFFのとき
        else:
            print('d')
            time += X

    # Aを入力したいとき
    else:
        # OFFのとき
        if not caps_lock:
            time1 = Y
            time2 = Z + X
            if time1 > time2:
                print('e')
                time += time1
            else:
                print('f')
                time += time2
                caps_lock = True
        # ONのとき
        else:
            print('g')
            time += X

# 出力
print(time)