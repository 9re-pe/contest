a, b = map(int, input().split())

cnt = 0
while a != 0 and b != 0:
    if a > b:
        cnt += a // b
        a = a % b
    else:
        cnt += b // a
        b = b % a

print(cnt-1)
