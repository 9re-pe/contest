def is_x_similler_to_y(x, y):
    if x == y:
        return True
    elif x == '1' and y == 'l':
        return True
    elif x == 'l' and y == '1':
        return True
    elif x == '0' and y == 'o':
        return True
    elif x == 'o' and y == '0':
        return True
    return False

# 入力
n = int(input())
s = input()
t = input()

ans = True
for i in range(n):
    if not is_x_similler_to_y(s[i], t[i]):
        ans = False
        break

# 出力
if ans:
    print('Yes')
else:
    print('No')

