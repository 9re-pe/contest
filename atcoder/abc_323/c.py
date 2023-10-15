n, m = map(int, input().split())
a = list(map(int, input().split()))

li_score = []
li_not_ans = []
for i in range(n):
    score = i + 1
    not_ans = []
    s = list(input())
    for j in range(m):
        if s[j] == 'o':
            score += a[j]
        else:
            not_ans.append(a[j])
    li_score.append(score)
    li_not_ans.append(not_ans)

max_score = max(li_score)
for i in range(n):
    score = li_score[i]
    not_ans = sorted(li_not_ans[i], reverse=True)

    cnt = 0
    while score < max_score:
        score += not_ans.pop(0)
        cnt += 1

    print(cnt)
