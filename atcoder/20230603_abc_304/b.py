n = input()
int_n = int(n)
n = list(n)

if int_n < 1000:
    pass
elif int_n < 10000: #9999
    n[3] = '0'
elif int_n < 100000: #99999
    n[3] = '0'
    n[4] = '0'
elif int_n < 1000000: #999999
    n[3] = '0'
    n[4] = '0'
    n[5] = '0'
elif int_n < 10000000:
    n[3] = '0'
    n[4] = '0'
    n[5] = '0'
    n[6] = '0'
elif int_n < 100000000:
    n[3] = '0'
    n[4] = '0'
    n[5] = '0'
    n[6] = '0'
    n[7] = '0'
else:
    n[3] = '0'
    n[4] = '0'
    n[5] = '0'
    n[6] = '0'
    n[7] = '0'
    n[8] = '0'

print(''.join(n))