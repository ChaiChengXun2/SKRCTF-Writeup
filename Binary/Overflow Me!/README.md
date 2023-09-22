# Overflow Me! - Binary Writeup

## Basic Information
**Category:** Binary  
**Points:** 20

## Objective

The "Overflow Me!" challenge presents an opportunity to familiarize yourself with stack buffer overflows. The objective is to overwrite a variable named "overflowMe" in the program's stack with the value `0xdeadbeef`.

## Solution

To successfully complete the "Overflow Me!" challenge, follow these steps:

1. **Prepare the Payload:**

   The goal is to write the value `0xdeadbeef` into the "overflowMe" variable. However, you can't directly input raw bytes into the program. To achieve this, you'll need to use the `echo` command to create the payload.

   ```bash
   echo -en '\xef\xbe\xad\xde'
   ```  

2. **Find the Offset :**

   You need to determine the offset at which you can overflow the "overflowMe" variable. In this case, it's 28 bytes, as stated in the source code.  

3. **Execute the Exploit :**

   Craft your exploit by padding with "A" characters (or any other character) to reach the offset and then append the payload.  

   ```bash
    echo -en 'AAAAAAAAAAAAAAAAAAAAAAAAAAAA\xef\xbe\xad\xde' | ./overflow2
   ```  

Flag: SKR{XXXXXXXXX}

**Challenge Accomplished**
