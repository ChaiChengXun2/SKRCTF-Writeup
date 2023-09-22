ASCII = "BTDJJ`Qmvt`1o4"
flag = ""

for character in ASCII:
    flag += chr(ord(character) - 1)

print(flag)
