# My First SQL - SQL Injection Challenge

## Basic Information
- **Category:** Web
- **Difficulty:** Easy
- **Points:** 20

## Solving
The "My First SQL" challenge introduces you to SQL injection, a common web security vulnerability. SQL injection occurs when user input is not properly sanitized, allowing attackers to manipulate SQL queries and potentially gain unauthorized access to a database. To prevent SQL injection, it's essential to sanitize inputs and escape user data before interacting with a database.

### Step-by-Step Guide

Follow these steps to solve the challenge:

1. **Identify the SQL Database:**
   - Through trial and error, determine that the challenge is using a MySQL database.

2. **Exploit the SQL Injection Vulnerability:**
   - Exploit the weak SQL implementation by injecting SQL code into the email and password fields.
   - Use the following SQL code:
     ```
     ' OR 1=1 --
     ```
     This input manipulates the SQL query to always return true, effectively bypassing authentication.

3. **Access the Flag:**
   - After successfully injecting the SQL code, the web application will grant access without a valid login.
   - Access the flag by copying and pasting it from the web application:
     ```
     SKR{XXXXXXXX}
     ```

**Challenge Completed!**

By exploiting the SQL injection vulnerability in the weak MySQL implementation, you successfully gained unauthorized access and retrieved the flag: "SKR{XXXXXXXX}."

This challenge highlights the importance of implementing proper input validation and sanitization to protect against SQL injection attacks in web applications.
