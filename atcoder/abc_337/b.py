s = input()

last = ""
ans = "Yes"
for char in s:
    if last == "A" or last == "":
        last = char
    elif last == "B":
        if char == 'A':
            ans = "No"
        else:
            last = char
    else:
        if char != 'C':
            ans = "No"

print(ans)


