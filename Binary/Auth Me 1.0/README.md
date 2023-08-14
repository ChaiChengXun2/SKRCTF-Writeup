# Auth Me 1.0

## Basic Information
Category: Binary    
Difficulty: Easy  
Points: 20  

## Solving
The concept of this challenge is to familiarirse yourself with overwriting stack content. (I think)
  
**Step 1:**  
Looking through the source code, we can see that ```gets``` is used. ```gets``` is deprecated because it does not check for buffer overflows. Therefore, it can be taken advantage of in this challenge. I don't know the actual way of solving challenges like these but through trial and error, I found that 29 random characters will break the program. The exact number might be different for you as the stack structure on your computer might be different.  

**Step 1:**  
Copy the flag and complete the challenge: ```SKR{OveRWr1te_loc4l_vAr14bLe_63ddcc}```

**SOLVED**  
