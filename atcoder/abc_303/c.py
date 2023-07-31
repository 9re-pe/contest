def is_on_item(now_position, item_position_list):
    if now_position in item_position_list:
        return True
    
    return False

def is_use_item(h, k):
    if h < k:
        return True
    return False

def use_item(h, k, now_position, item_position_list):
    if is_use_item(h, k):
        #print('use item!')
        h = k
        item_position_list.remove(now_position)
    
    return h, item_position_list

def get_position_after_move(command, now_position):
    if command == 'R':
        return (now_position[0]+1, now_position[1])
    elif command == 'L':
        return (now_position[0]-1, now_position[1])
    elif command == 'U':
        return (now_position[0], now_position[1]+1)
    elif command == 'D':
        return (now_position[0], now_position[1]-1)

# 入力
# n: 目標移動回数
# m: 回復アイテムの数
# h: HP
# k: 回復後のHP
# s: コマンド
N, M, h, K = map(int, input().split())
S = input()
# アイテムの座標
item_position_list = set()
for i in range(M):
    item_position_list.add(tuple(map(int, input().split())))

now_position = (0, 0)
for command in S:
    h -= 1
    
    if h < 0:
        break
    now_position = get_position_after_move(command, now_position)
    #print(now_position)
    #print(h)
    if is_on_item(now_position, item_position_list):
        #print('on item!')
        h, item_position_list = use_item(h, K, now_position, item_position_list)
    
# 出力
if (h >= 0):
    print('Yes')
else:
    print('No')