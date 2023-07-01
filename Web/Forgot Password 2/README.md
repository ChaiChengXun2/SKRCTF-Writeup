# Forgot Password 2

## Basic Information
Category: Web  
Difficulty: Easy  
Points: 20  

## Solving
The concept of of this challenge is similar to Forgot Password 1.
  
**Step 1:**  
Again, login validation should be done server-side instead of client-side. We can see that the JS logic for login is updated with MD5 hashing. It adds an extra layer of protection, but breaking MD5 is as easy as encrypting something with MD5. The hashed password is also visible in the source code. Reversing the hash will allow you to login.  
```Username: godam```  
```Password: imsohandsome```  

**Step 2:**   
Copy and paste the flag to complete the challenge  
```SKR{S1mple_P@ssw0rd_1s_3asY_70_Cr4cK_20f250}```  

**SOLVED**  
