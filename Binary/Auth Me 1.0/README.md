# Auth Me 1.0

## Basic Information
Category: Binary    
Difficulty: Medium  
Points: 20  

## Solving
The concept of this challenge is to familiarirse yourself with overwriting stack content. (I think)
  
**Step 1:**  
Looking through the source code, no vulnerable functions are present. But conveniently, the RAM contents are being printed out onto the console. Through trial and error, writing 0xdeadbeef into the console via little-endian solves the chalelnge.  

**Step 2:**  
Copy the flag and complete the challenge: ```SKR{Overfl0ww_Bin4ry_Byt35_52decc}```

**SOLVED**  
