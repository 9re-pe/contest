N = int(input().strip())
S = sorted(input().strip())

max_square = int((10**N)**0.5)

count = 0

for i in range(max_square + 1):
    square = i**2
    square_str = sorted(str(square).zfill(N))
    if square_str == S:
        count += 1

print(count)
