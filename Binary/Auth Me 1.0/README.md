# Auth Me 1.0 - Binary Writeup

## Basic Information
**Category:** Binary  
**Points:** 20

## Objective

The "Auth Me 1.0" challenge is designed to help you familiarize yourself with the concept of overflowing stack content in a binary. The objective is to exploit a vulnerability in the program that uses the `gets` function, which is known to be deprecated and prone to buffer overflows.

## Solution

To successfully complete the "Auth Me 1.0" challenge, follow these steps:

**Step 1: Identify the Vulnerability**

Looking through the source code provided for the binary, you can observe that the `gets` function is used to read user input. It's important to note that `gets` is deprecated and lacks buffer overflow protection, making it a potential security vulnerability.

**Step 2: Determine the Overflow Length**

Through trial and error, I found that you need to input 29 random characters to trigger a buffer overflow in the program. This means that if you input more than 29 characters, you will overwrite memory beyond the buffer, potentially affecting the program's execution.

**Step 3: Exploit the Vulnerability**

You can exploit the vulnerability by running the program and providing 29 arbitrary characters as input. Alternatively, you can use the `echo` command to automate this process. Here's an example of using `echo` to complete the challenge:

```bash
echo -en "AAAAAAAAAAAAAAAAAAAAAAAAAAAAA" | ./auth
```  

flag: SKR{XXXX}

**Challenge Finished**
