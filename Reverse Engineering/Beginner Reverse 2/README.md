# Beginner Reverse 2

## Basic Information
Category: Reverse Engineering    
Difficulty: Easy  
Points: 50  

## Solving
The concept of this challenge is to familiarise you with basic reverse engineering.
  
**Step 1:**    
SKRCTF provided us with a C program source code. Downloading and opening the C program, we can find a formula.  
```(pass * 2) - 666 = 2008```  

```atoi``` function tells us that the password is number based, and that there are no letters or special characters involved. By reversing the formula, we will be able to find the solution.

**Step 2:**   
Copy the flag and complete the challenge
```SKR{1337}```

**SOLVED**  
