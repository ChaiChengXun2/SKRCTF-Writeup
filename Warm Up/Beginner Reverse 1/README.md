# Beginner Reverse 1

## Basic Information
Category: Warm Up  
Difficulty: Beginner  
Points: 20  

## Solving
The main concept from this challenge is to understand the basics of reverse engineering. Reverse engineering involves understanding the source code and generate exploits for vulnerable programs.
  
**Step 1:**  
Download the following C file from SKRCTF 
Link to beginner.c: [beginner.c](https://skrctf.me/files/d48952dc599ecbd3becae90608887cab/beginner.c)

**Step 2:**  
View the file in your preferred IDE or 
```
cat beginner.c
```

**Step 3:**  
```strcmp``` is a function in C that compares two strings. It returns 0 if two strings are equal. In this case, the following code checks if user input is equal to ```P@ssw0rd1337```, hence the password
```
if (strcmp(password, "P@ssw0rd1337") == 0)
```

**Step 4:**  
Copy the following flag and complete the challenge
```SKR{P@ssw0rd1337}```

**SOLVED**
