part1 = "Spr3ue45"
part2 = "5PrcS3u"

# Reverse part2
reversedPart2 = part2[::-1]

flag = ""

# Combine parts in a specific order
for i in range(7):
    flag += part1[i]
    flag += reversedPart2[i]

# Add the last character
flag += '5'

print(flag)
