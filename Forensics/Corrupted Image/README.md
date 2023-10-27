# Corrupted Image - Forensics Challenge

## Basic Information
**Name:** Corrupted Image  
**Category:** Forensics  
**Points:** 20

## Objective

The "Corrupted Image" challenge is a forensics task. Your objective is to repair a corrupted image and then piece together the flag hidden within it.

## Solution

To successfully complete the "Corrupted Image" forensics challenge, follow these steps:

1. **Download the Corrupted Image:**
   - Upon downloading the provided file, you'll notice that it appears to be corrupted, as suggested by the challenge description.

2. **Repair the Corrupted Image:**
   - To repair the corrupted image, start by looking for the PNG file header. In PNG images, the headers typically contain "IHDR" and "IEND" markers. These markers are essential for identifying the start and end of a PNG image.

3. **Recover the Image:**
   - With the knowledge of the PNG file structure, try to fix the corrupted image by adding the necessary PNG headers.

4. **Retrieve the Hidden Flag:**
   - Once you have successfully repaired the image, open it and examine its contents. The flag is hidden within the image. Look for capital letters within the image, as these letters will spell out the flag.

5. **Flag Discovery:**
   - Piece together the capital letters found in the image to reveal the hidden flag.

Flag: skr{XXXXXXXXXX}

**Challenge Solved**  
