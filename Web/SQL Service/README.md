# SQL Service - SQL Injection Challenge

## Basic Information
- **Category:** Web
- **Difficulty:** Medium
- **Points:** 20

## Solving
The "SQL Service" challenge aims to familiarize you with SQL injection, a common web security vulnerability that occurs when user input is not properly sanitized.

### Step-by-Step Guide

Follow these steps to solve the challenge:

1. **Identify the SQL Injection Vulnerability:**
   - Start by recognizing that the challenge likely has a SQL injection vulnerability.
   - In SQL injection attacks, you can manipulate the application's SQL queries by injecting malicious SQL code into user input fields.

2. **Exploit the SQL Injection Vulnerability:**
   - Experiment with different SQL injection payloads to find one that works.
   - The payload that successfully works in this case is:
     ```
     ' or '' = '
     ```
     This payload manipulates the SQL query to always evaluate as true, bypassing any authentication checks.

3. **Access the Flag:**
   - Once you successfully inject the SQL payload, the application will grant you access without a valid login.
   - Copy and paste the flag to complete the challenge:
     ```
     SKR{XXXXXXXXXXX}
     ```

**Challenge Completed!**

By exploiting the SQL injection vulnerability with the provided payload, you gained unauthorized access and retrieved the flag: "SKR{XXXXXXXXXXX}."

This challenge underscores the importance of implementing proper input validation and escaping user input to prevent SQL injection attacks in web applications.
