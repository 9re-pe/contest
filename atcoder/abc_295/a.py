n = int(input())
w = set(list(input().split()))
kw = {'and', 'not', 'that', 'the', 'you'}

if len(w & kw):
    print('Yes')
else:
    print('No')
