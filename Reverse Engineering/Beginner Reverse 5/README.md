# Beginner Reverse 5 - Reverse Engineering Writeup

## Basic Information
**Category:** Reverse Engineering  
**Difficulty:** Easy  
**Points:** 50

## Solving

The "Beginner Reverse 5" challenge aims to familiarize you with ASCII encoding.

### Step 1: Understand the ASCII Transformation

To solve this challenge, follow these steps:

1. **Analyze the Password Check:**
   The program checks a password against the string ```"BTDJJ`Qmvt`1o4"```. However, it applies logic to subtract ```-1``` from each character during the check.

2. **ASCII Operations:**
   In the C programming language, characters can be treated as their ASCII values when subjected to mathematical operations. In this case, each character is decremented by 1.

3. **Python Code for Flag Extraction:**
   Use the following Python code to extract the flag:

   ```python
   ASCII = "BTDJJ`Qmvt`1o4"
   flag = ""

   for character in ASCII:
       flag += chr(ord(character) - 1)

   print(flag)
   ```
4. **Retrieve the Flag:**

flag: SKR{XXXXXXXX}

**Challenge Accomplished**  
