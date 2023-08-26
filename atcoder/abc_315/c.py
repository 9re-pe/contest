from collections import defaultdict


n = int(input())
fs = set()
dic1 = defaultdict(int)
dic2 = defaultdict(int)
for _ in range(n):
    f, s = map(int, input().split())
    fs.add(f)
    # 2位と比べる
    if dic2[f] <= s:
        # 1位と比べる
        if dic1[f] < s:
            dic2[f] = dic1[f]
            dic1[f] = s
        else:
            dic2[f] = s

same_max = 0
for f in fs:
    same_max = max(same_max, dic1[f]+dic2[f]//2)

if len(fs) == 1:
    print(same_max)
    exit(0)

val = dic1.values()
sorted_val = sorted(val, reverse=True)
diff_max = sorted_val[0] + sorted_val[1]

print(max(same_max, diff_max))
