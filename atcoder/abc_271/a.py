n = int(input())
hex_string = hex(n)[2:].upper()
formatted_hex = f"{hex_string:0>2}"
print(formatted_hex)
