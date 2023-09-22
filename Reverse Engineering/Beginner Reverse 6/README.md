# Beginner Reverse 6 - Reverse Engineering Writeup

## Basic Information
**Category:** Reverse Engineering  
**Difficulty:** Easy  
**Points:** 50

## Solving

The "Beginner Reverse 6" challenge focuses on understanding pointers and the ASCII table.

### Step 1: Analyze the Password Criteria

To solve this challenge, follow these steps:

1. **Understand the Password Criteria:**
   The challenge's password criteria provide hints about the password format. Examine these hints to deduce the password:
   - `length != 17` suggests that the password has a length of 17 characters.
   - `pass[0] != 'R'` indicates that the 1st character of the password is 'R'.
   - `pass[1] - pass[0] != -31 || pass[1] != pass[3]` tells us that the 2nd and 4th characters are the same value. The 2nd character can be calculated as the ASCII value of '-31 + 82,' which is '3' in ASCII.
   - `pass[4] != tolower(pass[0]) || pass[2] - pass[4] != 4` suggests that the 5th character is 'r,' and the 3rd character is '4 + 114,' which is 'v' in ASCII.
   - `pass[5] != '5' || pass[5] - pass[6] != 4` tells us that the 6th character is '5,' and the 7th character is '1.'
   - `pass[7] != pass[0] + 28 || pass[2] - pass[8] != 47` implies that the 8th character is 'n,' and the 9th character is 'G.'
   - `pass[9] != '_' || pass[12] != pass[9] || strncmp(pass+13,"Fun!",4) != 0 || strncmp(pass+10,"1s",2) != 0` reveals that the 10th and 13th characters are '_', and the final 4 characters are 'Fun!.' The 11th and 12th characters are reserved for '1s.'

2. **Combine the Clues:**
   By combining all the information gathered from the criteria, you can construct the password and, consequently, the flag.

### Step 2: Calculate the Flag

Combine the characters based on the criteria you've deduced to calculate the flag.

### Step 3: Retrieve the Flag

After completing the calculations, you'll obtain the flag: SKR{XXXXXXXX}

**Challenge Accomplished**  
