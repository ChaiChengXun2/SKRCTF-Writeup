# Beginner Reverse 1 - Warm Up Challenge

## Basic Information
- **Category:** Warm Up
- **Difficulty:** Beginner
- **Points:** 20

## Solving
The "Beginner Reverse 1" challenge aims to introduce you to the basics of reverse engineering. Reverse engineering involves understanding source code and generating exploits for vulnerable programs.

### Step-by-Step Guide

Follow these steps to solve the challenge:

1. **Download the C File:**
   - Download the provided C file from SKRCTF: [beginner.c](https://skrctf.me/files/d48952dc599ecbd3becae90608887cab/beginner.c)

2. **View the File:**
   - Open the downloaded C file in your preferred Integrated Development Environment (IDE) or simply view its contents using the `cat` command:
     ```
     cat beginner.c
     ```

3. **Understand the Code:**
   - In the source code, you'll find a `strcmp` function, which is a C function used to compare two strings.
   - This code segment checks if user input is equal to `"P@ssw0rd1337"`:
     ```c
     if (strcmp(password, "P@ssw0rd1337") == 0)
     ```

4. **Retrieve the Flag:**
   - After analyzing the code, you'll notice that the password is `"P@ssw0rd1337"`. Copy the flag to complete the challenge:
     ```
     SKR{XXXXXXXX}
     ```

**Challenge Completed!**

By identifying the password from the source code, you have successfully solved the "Beginner Reverse 1" challenge.
