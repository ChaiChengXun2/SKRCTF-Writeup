# My First SQL

## Basic Information
Category: Web  
Difficulty: Easy  
Points: 20  

## Solving
The concept of this challenge is to familiarise yourself with SQL injection. SQL injection is an exploit on weak SQL database implementation. To prevent SQL injection, always remember to sanitise inputs before submitting to servers and escape user inputs. 
  
**Step 1:**  
Through trial and error, I was able to find out that MySQL is used for this challenge. To exploit a weak MySQL implementation, type the following SQL into the email and password field.
```
' OR 1 = 1 -- 
```  

**Step 2:**   
Copy and paste the flag to complete the challenge  
```KR{Do_not_forget_to_escape_user_input_7f102f}```

**SOLVED**  
