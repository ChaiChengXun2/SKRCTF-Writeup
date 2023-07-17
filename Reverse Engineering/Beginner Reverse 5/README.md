# Beginner Reverse 5

## Basic Information
Category: Reverse Engineering    
Difficulty: Easy  
Points: 50  

## Solving
The concept of this challenge is to familiarise you with ASCII. 
  
**Step 1:**  
The program checks a password against ```BTDJJ`Qmvt`1o4``` but it has logic that  ```-1``` from each character. Characters in C can be treated as ASCII values when it is given a mathematical operation.   

Python Code that finds the flag   
```
ASCII = "BTDJJ`Qmvt`1o4"
flag = ""
for character in ASCII:
    flag += chr(ord(character) - 1)
    
print(flag)
```

**Step 2:**   
Copy the flag and complete the challenge
```SKR{ASCII_Plus_0n3}```

**SOLVED**  
