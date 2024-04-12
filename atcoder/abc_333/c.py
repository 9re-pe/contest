n = int(input())
max_digit = 12
repunits = [int("1" * (i+1)) for i in range(max_digit)]

s = set()
for i in range(max_digit):
    for j in range(max_digit):
        for k in range(max_digit):
            s.add((repunits[i] + repunits[j] + repunits[k]))

li = list(s)
li.sort()
print(li[n-1])
