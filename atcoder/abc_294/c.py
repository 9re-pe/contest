n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_ans = []
b_ans = []
a_cnt = 0
b_cnt = 0
for i in range(1, n+m+1):
    if a_cnt > n-1:
        b_ans.append(i)
        b_cnt += 1
    elif b_cnt > m-1:
        a_ans.append(i)
        a_cnt += 1
    elif a[a_cnt] < b[b_cnt]:
        a_ans.append(i)
        a_cnt += 1
    else:
        b_ans.append(i)
        b_cnt += 1

print(*a_ans)
print(*b_ans)
