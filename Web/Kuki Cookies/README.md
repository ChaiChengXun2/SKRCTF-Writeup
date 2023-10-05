# Kuki Cookies - CTF Challenge Writeup

Challenge: Kuki Cookies
Points: 20
Category: Web

## Objective
The objective of the Kuki Cookies challenge is to understand how to read cookies in a web environment.

## Solution
To successfully complete this challenge, follow these steps:

1. **Read the provided cookie**: In a web instance, you will have access to a cookie. You need to read the content of this cookie.

2. **Flag URL encoding**: When you inspect the cookie, you may notice that the flag appears incorrect upon submission. This is because the flag is URL encoded. URL encoding is a way of representing special characters within a URL.

3. **Decode the flag**: To get the actual flag, you need to decode the URL-encoded flag. In many cases, you can use a URL decoding tool or a simple script to perform this operation.