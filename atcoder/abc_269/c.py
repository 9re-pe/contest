n = int(input())
n_bit = bin(n)[2:]
n_bit = n_bit[::-1]  # 反転

x = ['']
for i in range(len(n_bit)):
    new_x = []

    if n_bit[i] == '0':
        for a in x:
            new_x.append('0' + a)

    else:
        for a in x:
            new_x.append('0' + a)
            new_x.append('1' + a)

    x = new_x

x.sort()
for ans in x:
    print(int(ans, 2))
