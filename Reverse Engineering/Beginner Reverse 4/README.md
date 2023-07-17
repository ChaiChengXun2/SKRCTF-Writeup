# Beginner Reverse 4

## Basic Information
Category: Reverse Engineering    
Difficulty: Easy  
Points: 50  

## Solving
The concept of this challenge is to familiarise you with C programming language and reverse engineering, encouraging you to read source code and find ways to exploit it.
  
**Step 1:**  
There are two ```for``` loops in the given C source code. Both increments by two in every iteration, but one in reverse.  

Python Code that finds the flag   
```
part1 = "Spr3ue45"
part2 = "5PrcS3u"

reversedPart2 = part2[::-1]

flag = ""

for i in range(7):
    flag += part1[i]
    flag += reversedPart2[i]

print(flag + '5')
```


**Step 2:**   
Copy the flag and complete the challenge
```SKR{Sup3rS3cureP455}```

**SOLVED**  
