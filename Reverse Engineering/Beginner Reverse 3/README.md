# Beginner Reverse 3

## Basic Information
Category: Reverse Engineering    
Difficulty: Easy  
Points: 50  

## Solving
The concept of this challenge is to familiarise you with pointers in C programming language.
  
**Step 1:**  
Pointers in C are references to a memory location in the program. By looking through the C code, we can find the flag.  
```strlen(pass) != 14``` tells us that the password is of length 14  
```strncmp(pass+2,"cur3", 4) != 0``` tells us that the 3rd, 4th, 5th and 6th character of the password is 'cur3'  
```strncmp(pass,"S3", 2) != 0``` tells us that the 1st and 2nd character of the password is 'S3'  
```strncmp(pass+10,"w0rd", 4``` tells us that the 11th, 12th, 13th, and 14th character in the password is 'w0rd'  
```strncmp(pass+6,"Pa$$", 4``` tells us that the 7th, 8th, 9th, and 10th character in the password is 'Pa$$'  
Putting together the password, we get the flag


**Step 2:**   
Copy the flag and complete the challenge
```SKR{S3cur3Pa$$w0rd}```

**SOLVED**  
