def is_one_replacement_away(a: str, b: str) -> bool:
    diff_count = 0
    for char_a, char_b in zip(a, b):
        if char_a != char_b:
            diff_count += 1
            if diff_count > 1:
                return False

    return diff_count == 1


def is_one_insert_away(a: str, b: str) -> bool:
    diff_count = 0
    i, j = 0, 0

    while i < len(a) and j < len(b):
        if a[i] != b[j]:
            if diff_count > 0:
                return False

            diff_count += 1
            j += 1  # b has one more character, so increment j
        else:
            i += 1
            j += 1

    return True


def is_one_deletion_away(a: str, b: str) -> bool:
    diff_count = 0
    i, j = 0, 0

    while i < len(a) and j < len(b):
        if a[i] != b[j]:
            if diff_count > 0:
                return False

            diff_count += 1
            i += 1  # a has one more character, so increment i
        else:
            i += 1
            j += 1

    return True


n, t = input().split()
n = int(n)
l = len(t)

ans = []
for i in range(n):
    s = input()

    if len(s) == l:
        if s == t:
            ans.append(i+1)
            continue
        elif is_one_replacement_away(t, s):
            ans.append(i+1)
            continue
        else:
            continue

    if len(s) == l + 1:
        if is_one_insert_away(t, s):
            ans.append(i+1)
            continue
        else:
            continue

    if len(s) == l - 1:
        if is_one_deletion_away(t, s):
            ans.append(i+1)
            continue
        else:
            continue


print(len(ans))
print(*ans)
