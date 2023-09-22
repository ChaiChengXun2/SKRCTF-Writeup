# Forgot Password - Easy Web Challenge

## Basic Information
- **Category:** Web
- **Difficulty:** Easy
- **Points:** 20

## Solving
The "Forgot Password" challenge aims to teach you about web security and the importance of server-side validation for authentication.

### Step-by-Step Guide

Follow these steps to solve the challenge:

1. **Inspect the Source Code:**
   - Right-click on the webpage and select "View Page Source" or press `CTRL+U` to access the HTML source code.
   - Examine the HTML, CSS, and JavaScript code used to build the webpage.

2. **Analyze Client-Side Validation:**
   - Inside the JavaScript code, you'll notice that all aspects of login validation are handled on the client side.
   - There is no server-side validation to ensure secure authentication.

3. **Retrieve Login Credentials:**
   - Extract the login credentials from the JavaScript code:
     - Username: `godam`
     - Password: `Sup3rSecr3t4ndS3cur3P@s$W0rD`

4. **Log In:**
   - Use the retrieved credentials to log in:
     - Username: `godam`
     - Password: `Sup3rSecr3t4ndS3cur3P@s$W0rD`

5. **Retrieve the Flag:**
   - After successfully logging in, you can access the flag:
     ```
     SKR{XXXXXXXXXXXX}
     ```

**Challenge Completed!**

By inspecting the source code, analyzing the lack of server-side validation, and using the provided credentials, you successfully logged in and retrieved the flag: "SKR{XXXXXXXXXXXX}."

This challenge highlights the importance of server-side validation for secure authentication and the risks of relying solely on client-side validation.

Remember these lessons for future web security challenges.
