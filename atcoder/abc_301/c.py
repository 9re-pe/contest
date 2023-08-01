from collections import defaultdict
import string

s = input()
t = input()
s_dic = defaultdict(int)
t_dic = defaultdict(int)

for i in range(len(s)):
    s_dic[s[i]] += 1
    t_dic[t[i]] += 1

atcoder = {'a', 't', 'c', 'o', 'd', 'e', 'r'}

ans = 'Yes'
s_at = s_dic['@']
t_at = t_dic['@']
for c in string.ascii_lowercase:
    if s_dic[c] != t_dic[c]:
        if c in atcoder:
            if s_dic[c] > t_dic[c]:
                t_at -= s_dic[c] - t_dic[c]
                if t_at < 0:
                    ans = 'No'
            else:
                s_at -= t_dic[c] - s_dic[c]
                if s_at < 0:
                    ans = 'No'
        else:
            ans = 'No'

print(ans)
