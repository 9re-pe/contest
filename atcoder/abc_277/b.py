suit = {'H', 'D', 'C', 'S'}
num = {'A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K'}
card = set()

n = int(input())
ans = 'Yes'
for _ in range(n):
    s = input()

    if s[0] not in suit:
        ans = 'No'

    if s[1] not in num:
        ans = 'No'

    if s in card:
        ans = 'No'

    card.add(s)

print(ans)
