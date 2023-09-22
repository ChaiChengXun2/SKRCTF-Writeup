# Secret URL - Web Challenge

## Basic Information
- **Category:** Web
- **Difficulty:** Medium
- **Points:** 20

## Solving
The "Secret URL" challenge introduces you to the concept of the robots.txt file, a commonly used tool for controlling web crawlers' access to different parts of a website. This file can reveal hidden paths or resources on a website that might not be immediately visible.

### Step-by-Step Guide

Follow these steps to solve the challenge:

1. **Explore Robots.txt:**
   - Start by visiting the URL provided to you.
   - Append `/robots.txt` to the URL, creating a new URL like this: `URL/robots.txt`.
   - Accessing this URL will reveal the website's `robots.txt` file, which contains instructions for web crawlers.

2. **Discover Disallowed Resources:**
   - Within the `robots.txt` file, you may find links or paths that are disallowed or restricted for web crawlers. These links could be of interest.

3. **Investigate Suspicious Paths:**
   - After identifying a disallowed URI in the `robots.txt` file, append it to the original URL.
   - For example, if the disallowed URI is `916767aa91f2f5d6cb2ab7b13a4eae55.html`, access it by combining it with the original URL: `URL/916767aa91f2f5d6cb2ab7b13a4eae55.html`.

4. **Access the Flag:**
   - By following the disallowed path, you will discover the flag.
   - Copy and paste the flag into the challenge field to complete it:
     ```
     SKR{XXXXXXXXXXX}
     ```

**Challenge Completed!**

By exploring the `robots.txt` file and following the disallowed path, you unveiled the hidden flag: "SKR{XXXXXXXXXXX}."

This challenge illustrates how web developers use `robots.txt` to control the behavior of web crawlers and how you can uncover hidden resources by examining this file.
