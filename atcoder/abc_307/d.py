# TLE

# n = int(input())
# s = list(input())
 
# stack = []
# for i in range(n):
#     # (が出てきたらプッシュ
#     if s[i] == '(':
#         stack.append(i)
#     # )が出てきたらポップして(から)までを削除
#     if s[i] == ')' and len(stack) != 0:
#         start = stack.pop()
#         end = i
#         # 文字を0に書き換えて削除を扱う
#         for j in range(start, end+1):
#             s[j] = 0
 
# ans = ''
# for char in s:
#     if char != 0:
#         ans += char
 
# print(ans)


from collections import deque
 
n = int(input())
s = list(input())

ans = [] 
stack = deque([])
for i, c in enumerate(s):
    if c == '(':
        stack.append(i)
    if c == ')' and len(stack) != 0:
        start = stack.pop()
        ans = ans[:start]
        continue
    ans.append(s[i])
 
print(''.join(ans))

