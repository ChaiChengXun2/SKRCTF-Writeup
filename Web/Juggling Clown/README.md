# Juggling Clown - Insecure PHP Comparison Challenge

## Basic Information
- **Category:** Web
- **Difficulty:** Medium
- **Points:** 20

## Solving
The "Juggling Clown" challenge aims to familiarize you with insecure PHP code and the concept of loose and strict comparison.

### Step-by-Step Guide

Follow these steps to solve the challenge:

1. **Inspect the HTML Source Code:**
   - Open the webpage and view the HTML source code.
   - Look for hidden information or clues within the page.

2. **Find the Hidden PHP Code:**
   - Inside the HTML source code, discover a hidden link that leads to the PHP code behind the webpage.

3. **Identify the Vulnerability:**
   - Analyze the PHP code and identify the vulnerability. It uses a loose comparison (`==`) instead of a strict comparison (`===`) to compare a string with user input:
     ```php
     if (strcmp($answer, $_GET["answer"]) == 0)
     ```
     The vulnerability allows for different ways to exploit the string comparison.

4. **Exploit the Loose Comparison:**
   - In PHP, when comparing a string with an array using `strcmp`, it returns `NULL`. This happens because `strcmp` expects strings as arguments. When provided with a non-string argument (an array), PHP attempts to convert it into a string but sometimes fails. This failure results in `NULL`.
   - In a loose comparison, comparing `NULL` with `0` always returns true.
   - Exploit the PHP code by using the following URL format:
     ```
     URL/index.php?answer[]
     ```

5. **Retrieve the Flag:**
   - After successfully exploiting the loose comparison, the PHP code will output the flag:
     ```
     SKR{XXXXXXXXXX}
     ```

**Challenge Completed!**

By identifying the loose comparison vulnerability in the PHP code and exploiting it with a specific URL format, you successfully retrieved the flag: "SKR{XXXXXXXXXXXXX}."

This challenge highlights the importance of using strict comparisons (`===`) for secure PHP code to prevent unintended vulnerabilities.
