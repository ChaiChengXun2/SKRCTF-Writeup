# Beginner Reverse 2 - Reverse Engineering Writeup

## Basic Information
**Category:** Reverse Engineering  
**Difficulty:** Easy  
**Points:** 50

## Solving

The "Beginner Reverse 2" challenge is designed to introduce you to basic reverse engineering concepts.

### Step 1: Analyze the C Program Source Code

To solve this challenge, follow these steps:

1. **Obtain the Source Code:**
   SKRCTF has provided a C program source code. Start by downloading and opening this C program.

2. **Decipher the Formula:**
   Within the C program source code, you'll find a formula that looks like this: ```(pass * 2) - 666 = 2008```  

3. **Identify the Password Format:**
   The `atoi` function used in the code hints that the password is based on numbers, with no letters or special characters involved. This means you need to work with numeric values to find the solution.

4. **Reverse the formula**  

flag: SKR{XXXXXXXX}

**Challenge Accomplished**  
