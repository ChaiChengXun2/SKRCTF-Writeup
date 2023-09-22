# Beginner Reverse 3 - Reverse Engineering Writeup

## Basic Information
**Category:** Reverse Engineering  
**Difficulty:** Easy  
**Points:** 50

## Solving

The "Beginner Reverse 3" challenge is designed to help you understand pointers in the C programming language.

### Step 1: Analyze the C Code

To solve this challenge, follow these steps:

1. **Understand Pointers:**
   In C, pointers are references to memory locations in the program. By examining the provided C code, we can uncover the flag.

2. **Analyze the Code:**
   Inspect the C code for clues about the password:
   - `strlen(pass) != 14` suggests that the password has a length of 14 characters.
   - `strncmp(pass+2,"cur3", 4) != 0` indicates that the 3rd, 4th, 5th, and 6th characters of the password are 'cur3'.
   - `strncmp(pass,"S3", 2) != 0` tells us that the 1st and 2nd characters of the password are 'S3'.
   - `strncmp(pass+10,"w0rd", 4)` implies that the 11th, 12th, 13th, and 14th characters in the password are 'w0rd'.
   - `strncmp(pass+6,"Pa$$", 4)` reveals that the 7th, 8th, 9th, and 10th characters in the password are 'Pa$$'.

3. **Reconstruct the Password:**
   By combining the information gathered from the code, we can construct the password, which is also the flag.

### Step 2: Calculate the Flag

Based on the code analysis, the password/flag is constructed as follows:
- The first two characters are 'S3'.
- The next four characters are 'cur3'.
- The following four characters are 'Pa$$'.
- The last four characters are 'w0rd'.

### Step 3: Retrieve the Flag

You've reconstructed the flag based on the password criteria. Copy the flag and use it to complete the challenge:

flag: SKR{XXXXXXXX}

**Challenge Accomplished**  

