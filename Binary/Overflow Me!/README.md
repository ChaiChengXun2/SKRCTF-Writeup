# Overflow Me!

## Basic Information
Category: Binary    
Difficulty: Medium   
Points: 20  

## Solving
The concept of this challenge is to familiarirse yourself with overwriting stack content. (I think)
  
**Step 1:**  
Looking through the soruce code, we don't see any vulnerable functions, but conveniently, the source codes prints out RAM content in hexadecimal and decimal values. The hints also provided us with the linux command to inject binary values into the program.   

**Step 2:**  
At least on my side, the system uses little-endian therefore the binary had to be reversed. Using 28 "A"s and a reversed 0xdeadbeef solves the challenge.  

**Step 3:**  
Copy the flag and complete the challenge: ```SKR{Overfl0ww_Bin4ry_Byt35_52decc}```

**SOLVED**  
