N = int(input())
s_list = []
a_list = []
for i in range(N):
    s, a = input().split()
    s_list.append(s)
    a_list.append(int(a))

min_i = a_list.index(min(a_list))

for j in range(N):
    i = min_i + j
    if i > N - 1:
        i = i - N
    print(s_list[i])
