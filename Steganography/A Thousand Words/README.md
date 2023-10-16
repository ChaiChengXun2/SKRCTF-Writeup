# A Thousand Words - Steganography Challenge

## Basic Information
**Name:** A Thousand Words  
**Category:** Steganography  
**Points:** 20

## Objective

The "A Thousand Words" challenge is a steganography task that involves finding a hidden flag within images and textual data. Your objective is to extract the flag from a sequence of images and text strings.

## Solution

To successfully complete the "A Thousand Words" steganography challenge, follow these steps:

1. **Examine the Provided Picture:**
   - You are given an image that features the GitHub logo. This image is the starting point of the challenge.

2. **Use Strings on the Image:**
   - Perform a basic analysis on the image by using the `strings` command. 

3. **Find a GitHub Repository:**
   - Through the `strings` analysis, you will discover a reference to a GitHub repository. Take note of the repository's URL.

4. **Visit the GitHub Repository:**
   - Go to the GitHub repository mentioned in the discovered text strings. This repository contains additional content relevant to the challenge.

5. **Discover Another Image:**
   - Inside the GitHub repository, you will come across another image that displays the text "not the flag." While this image may not appear to be the flag itself, download it for further investigation.

6. **Use Strings on the Second Image:**
   - Perform another `strings` analysis on the downloaded image. This analysis will reveal hidden text data within the image.

7. **Uncover the Base64 Encoded Flag:**
   - Within the second image's text data, you will find a base64-encoded flag. Decode the base64 text to reveal the hidden flag.

Flag: skr{XXXXXXXXXX}

**Challenge Solved**  
