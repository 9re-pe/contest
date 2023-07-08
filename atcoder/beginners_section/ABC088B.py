n = int(input())
alist = list(map(int, input().split()))
alist.sort(reverse = True)

alice = 0
bob = 0
alice_turn = True
for a in alist:
    if alice_turn:
        alice += a
        alice_turn = False
    else:
        bob += a
        alice_turn = True

print(alice - bob)

