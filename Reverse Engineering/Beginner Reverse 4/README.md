# Beginner Reverse 4 - Reverse Engineering Writeup

## Basic Information
**Category:** Reverse Engineering  
**Difficulty:** Easy  
**Points:** 50

## Solving

The "Beginner Reverse 4" challenge aims to familiarize you with the C programming language and reverse engineering. It encourages you to read source code and find ways to exploit it.

### Step 1: Analyze the Source Code

To solve this challenge, follow these steps:

1. **Examine the C Source Code:**
   The provided C source code contains two `for` loops. Both loops increment by two in each iteration, but one of them is in reverse.

2. **Python Code for Flag Extraction:**
   Use the following Python code to extract the flag:

   ```python
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
   ```  
3. **Calculate the Flag:**
   Run the provided Python code to calculate the flag. It combines the two parts of the flag based on specific characters from each part.

flag: SKR{XXXXXXXX}

**Challenge Accomplished**  
