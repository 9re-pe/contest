def n_pertisipate_member(t, company):
    """
    参加できるメンバーの数を返す
    参加できない時刻の場合は0を返す
    :param t: 会議開始時刻(世界標準時)
    :param company: (w, x)
    :return: int
    """

    w, x = company
    if 9 <= (t + x) % 24 <= 17:
        return w
    else:
        return 0


n = int(input())

companies = []
for _ in range(n):
    w, x = map(int, input().split())
    companies.append((w, x))

ans = 0
for t in range(24):
    cnt = 0
    for company in companies:
        cnt += n_pertisipate_member(t, company)
    ans = max(ans, cnt)

print(ans)
