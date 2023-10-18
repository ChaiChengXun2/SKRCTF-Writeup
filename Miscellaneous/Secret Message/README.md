# Secret Message - Miscellaneous Challenge

## Basic Information
**Name:** Secret Message  
**Category:** Miscellaneous  
**Points:** 20

## Objective

The "Secret Message" challenge is a miscellaneous task that involves decoding a hidden message. Your objective is to decode a message that has been encoded in Base64 and uncover the hidden flag.

## Solution

To successfully complete the "Secret Message" miscellaneous challenge, follow these steps:

1. **Decode the Base64 Message:**
   - The challenge provides you with a message that has been encoded in Base64. The hint suggests that this Base64 message can be converted into a file.

2. **Use CyberChef or Linux Command:**
   - You have two options to decode the Base64 message. The first option is to use an online tool like CyberChef, which can easily convert Base64 to a file.
![Cyberchef Base64 to File](<base64 to file.png>)
   - The second option is to use a Linux command. You can run the following command in your terminal:
     ```shell
     base64 -d <<< <base64_message> > output
     ```
     Replace `<base64_message>` with the provided Base64 message and save the decoded content in an "output" file.

3. **Decompress the Gzip File:**
   - After decoding the Base64 message, you may discover that it represents a Gzip file.

4. **Decompression:**
   - To access the content within the Gzip file, decompress it using a tool like `gunzip`.

5. **Retrieve the Flag:**
   - Once you've successfully decompressed the Gzip file, explore its contents to locate the hidden flag.

Flag: skr{XXXXXXXXXX}

**Challenge Solved**  
