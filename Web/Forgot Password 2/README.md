# Forgot Password 2 - Easy Web Challenge

## Basic Information
- **Category:** Web
- **Difficulty:** Easy
- **Points:** 20

## Solving
The "Forgot Password 2" challenge builds upon the concepts introduced in "Forgot Password 1."

### Step-by-Step Guide

Follow these steps to solve the challenge:

1. **Analyze Client-Side Validation:**
   - Similar to "Forgot Password 1," the challenge relies on client-side validation, which is not secure.
   - JavaScript logic for login now includes MD5 hashing for password validation, adding an extra layer of protection.
   - However, the hashed password is still visible in the source code.

2. **Reverse MD5 Hash:**
   - To bypass the login, you need to reverse the MD5 hash of the password.
   - Given username: `godam` and password: `imsohandsome`.

3. **Log In:**
   - Use the following credentials to log in:
     - Username: `godam`
     - Password: `imsohandsome`

4. **Retrieve the Flag:**
   - After successfully logging in, you can access the flag.
     ```
     SKR{XXXXXXXXXX}
     ```

**Challenge Completed!**

By analyzing the client-side validation, reversing the MD5 hash, and using the provided credentials, you successfully logged in and retrieved the flag: "SKR{XXXXXXXXXX}." This demonstrates the importance of server-side validation for secure authentication.

Remember to apply these principles in future web security challenges.
