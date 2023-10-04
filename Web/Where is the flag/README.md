# Where is the Flag? - Web Challenge

## Basic Information
- **Category:** Web
- **Difficulty:** Easy
- **Points:** 20

## Solving
The "Where is the Flag?" challenge is designed to introduce you to HTML and CSS and demonstrate how changes in web styling can reveal hidden content.

### Step-by-Step Guide

Follow these steps to solve the challenge:

1. **Inspect the Webpage:**
   - Open the provided webpage and inspect it using your browser's developer tools.
   - Alternatively, view the CSS files associated with the webpage.

2. **Explore the CSS Rules:**
   - In the CSS files or within the browser's developer tools, locate a CSS rule that affects the `body` element.
   - There, you will find a CSS rule similar to the following:
     ```css
     .flag::after {
         content: " SKR{XXXXXXXXXXX}";
         color: white;
     }
     ```
   - This CSS rule inserts the flag as content and sets its color to white, making it invisible against the background.

3. **Reveal the Flag:**
   - By examining the CSS, you discover the hidden flag.
   - Copy the flag text:
     ```
     SKR{XXXXXXXXXXX}
     ```
   - Paste the flag into the challenge field to complete it.

**Challenge Completed!**

You successfully solved the "Where is the Flag?" challenge by inspecting the webpage's HTML and CSS. By identifying the CSS rule responsible for hiding the flag's text, you revealed the hidden flag: "SKR{XXXXXXXXXXX}."

This challenge illustrates how web styling, particularly CSS rules, can be used to hide or reveal content on a
