# Steganography 2 - Steganography Challenge

## Basic Information
**Name:** Steganography 2  
**Category:** Steganography  
**Points:** 150

## Objective

The "Steganography 2" challenge is a steganography task that involves extracting a hidden flag from an image using a provided password. Your objective is to use the given password to reveal the flag concealed within the image.

## Solution

To successfully complete the "Steganography 2" steganography challenge, follow these steps:

1. **Obtain the Password:**
   - In the challenge description, you are provided with a password. This password will be essential for extracting the hidden flag from the image.

2. **Use Steghide Tool:**
   - Since you have the password, the first step is to use a steganography tool like Steghide. Steghide is a tool designed to embed and extract data from images.

3. **Extract Data from the Image:**
   - Use the Steghide command to extract data from the image file: `steghide --extract -sf <file>`.
   - Replace `<file>` with the name of the image file that you've obtained as part of the challenge.

4. **Provide the Password:**
   - As part of the extraction process, you'll be prompted to provide the password. Enter the password that was provided in the challenge description.

5. **Hidden Flag Extraction:**
   - After providing the correct password, Steghide will use it to enable the extraction process. You'll notice that a file is being written during this process.

6. **Retrieve the Flag:**
   - Once the extraction process is complete, check the output file that was created. The hidden flag is contained within this file.

Flag: skr{XXXXXXXXXX}

**Challenge Solved**  
