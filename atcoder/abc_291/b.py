n = int(input())
x = list(map(int, input().split()))
x.sort()

average = sum(x[n:-n]) / (3 * n)
print(average)
