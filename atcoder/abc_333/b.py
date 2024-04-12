s1, s2 = tuple(list(input()))
t1, t2 = tuple(list(input()))

c2i = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
}

s1 = c2i[s1]
s2 = c2i[s2]
t1 = c2i[t1]
t2 = c2i[t2]


def is_near(a, b):
    return abs(a - b) in {1, 4}


if is_near(s1, s2) and is_near(t1, t2):
    print("Yes")
elif not is_near(s1, s2) and not is_near(t1, t2):
    print("Yes")
else:
    print("No")
